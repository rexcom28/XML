
import decimal
import json
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View

from Clientes.models import Configuracion
from . models import Parte, Ingreso, Ingreso_Conceptos, Impuesto_PartidasIngreso, CfdiRelacionados_Ingreso, CfdiRelacionados_Ingreso
from . forms import ParteForm, IngresoForm,IngresoConceptoForm,IngresoFomSet
from django.views.generic.edit import * 
from django.views.generic import ListView, DeleteView
from django.db.models import Sum
import datetime
def index(request):
    h = Parte.objects.all()
    
    f=''
    for j in h:
        f += str(j)
        
    return HttpResponse(f)

class DeleteIngresoView(LoginRequiredMixin, DeleteView):
    model = Ingreso
    
    def get_success_url(self):
        url = reverse_lazy('ingreso-list-view')
        return url

class ParteCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)
    model = Parte
    form_class = ParteForm

class IngresoCreateView(LoginRequiredMixin, CreateView):
    model = Ingreso
    success_url = reverse_lazy('ingreso-list-view')
    template_name = 'Ingreso.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(IngresoCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ingreso_inline_formset'] = IngresoFomSet(self.request.POST)
        else:            
            context['form'] = IngresoForm(initial=self.get_Emisor())
            
            context['ingreso_inline_formset'] = IngresoFomSet()
        return context
    def get_Emisor(self):
        Emi = Configuracion.objects.get(id=1)
        ini = {
            'Rfc_Emi':Emi.RFC,
            'Nombre_Emi':Emi.Nombre,
            'RegimenFiscal_Emi':Emi.Regimen,
            'NoCertificado':Emi.Num_Certificado,
            'SubTotal':0,
            'Total': 0,
            'IVA':0,
            'IVA_Ret':0,
            'ISR':0,

        }
        
        return ini
    def suma(self, form, formset):        
        Importe = decimal.Decimal(0.0000)
        Descuento = decimal.Decimal(0.0000)        
        for f  in formset :            
            if f :
                if len(f.cleaned_data) != 0:
                    if f.cleaned_data['Descuento'] == 0:
                        Importe = f.cleaned_data['Cantidad'] * f.cleaned_data['ValorUnitario']
                    else:
                        Importe = f.cleaned_data['Cantidad'] * f.cleaned_data['ValorUnitario']
                        
                        des = f.cleaned_data.get('Descuento') if not f.cleaned_data.get('Descuento') == None else 0
                        Importe -= des 
                        Descuento += des
                    f.instance.Importe= Importe                                        
                    print('--------',f.cleaned_data)
        form.instance.Descuento = Descuento                
        form.instance.Total = Importe
        return form, formset

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['ingreso_inline_formset']
        print('forms: ', formset.is_valid() , form.is_valid())
        if formset.is_valid() and form.is_valid():            
            form, formset = self.suma(form, formset)
            
            response = super(IngresoCreateView, self).form_valid(form)            
            form.save()            
            formset.instance=self.object
            formset.save()

            return response
        else:            
            return super().form_invalid(form)

class IngresoUpdateView(LoginRequiredMixin, UpdateView):

    model = Ingreso
    template_name = 'Ingreso.html'
    form_class = IngresoForm
    #success_url = 
    def post(self, request, *args, **kwargs):
        print(self.request)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        formset =  Ingreso_Conceptos.objects.values('Importe', 'Descuento').filter(Comprobante__pk=self.kwargs['pk']).aggregate(
            Importe_s = Sum('Importe'),
            Descuento_s = Sum('Descuento')
        )
        qss = list(
            Ingreso_Conceptos.objects.values('id').filter(Comprobante__pk=self.kwargs['pk'])
            )
        qss = [l['id'] for l in qss if 'id' in l]        
        IVA = Impuesto_PartidasIngreso.objects.values('Importe', 'Impuesto', 'Tipo_T_R').filter(Imp_Partida_id__in=qss, Tipo_T_R='TRASLADO', Impuesto='002')
        IVA_Ret = Impuesto_PartidasIngreso.objects.values('Importe', 'Impuesto', 'Tipo_T_R').filter(Imp_Partida_id__in=qss, Tipo_T_R='RETENCION', Impuesto='002')
        ISR = Impuesto_PartidasIngreso.objects.values('Importe', 'Impuesto', 'Tipo_T_R').filter(Imp_Partida_id__in=qss, Tipo_T_R='RETENCION', Impuesto='001')
        #print('IVA',IVA , 'IVA_Ret', IVA_Ret, 'ISR', ISR)

        #print('Updating form ingreso ALV', formset)
        form.instance.SubTotal = formset['Importe_s']                
        form.instance.Descuento = formset['Descuento_s']
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        
        context = super(IngresoUpdateView, self).get_context_data(**kwargs)        
        context["qs"]= Ingreso_Conceptos.objects.filter(Comprobante__pk=self.kwargs['pk'])
        
        #no es necesario ya se hace por json resp CFDI_RelacionadoView 
        #context['DocRel']= CfdiRelacionados_Ingreso.objects.filter(CFDI_Rel__pk=self.kwargs['pk'])
        context['Impuestos']= self.ImpuestosPartidas() 
        context['id']= self.kwargs['pk']
        return context
    def ImpuestosPartidas(self, **kwargs):
        
        qs = list(
            Ingreso_Conceptos.objects.values('id').filter(Comprobante__pk=self.kwargs['pk'])
            )
        qs = [l['id'] for l in qs if 'id' in l]        
        qs = Impuesto_PartidasIngreso.objects.filter(Imp_Partida_id__in=qs)
        
        return qs

    def get_success_url(self):
        url = reverse_lazy('ingreso-list-view')
        return url

class IngresoConceptos_ListView(LoginRequiredMixin, ListView):
    model = Ingreso_Conceptos
    template_name = 'Comp/ingreso_concepto_list.html'

    def get_context_data(self, **kwargs):
        context = super(IngresoConceptos_ListView, self).get_context_data(**kwargs)
        context['id']= self.kwargs['pk']  
        context['Impuestos']= self.ImpuestosPartidas()      
        return context

    def get_queryset(self, **kwargs):
        
        qs = Ingreso_Conceptos.objects.filter(Comprobante__pk=self.kwargs['pk'])
        return qs
    def ImpuestosPartidas(self, **kwargs):
        
        qs = list(Ingreso_Conceptos.objects.values('id').filter(Comprobante__pk=self.kwargs['pk']))
        qs = [l['id'] for l in qs if 'id' in l]        
        qs = Impuesto_PartidasIngreso.objects.filter(Imp_Partida_id__in=qs)
        
        return qs


class IngresoListView(LoginRequiredMixin, ListView):
    model = Ingreso
    template_name = 'Comp/ingreso_list.html'

    def get_context_data(self, **kwargs):
        context=super(IngresoListView, self).get_context_data(**kwargs)        
        return context



class ConceptoUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingreso_Conceptos
    template_name = "Comp/ingreso_conceptos_form_update2.html"
    form_class = IngresoConceptoForm
    def get_context_data(self, **kwargs):
        context = super(ConceptoUpdateView, self).get_context_data(**kwargs)
        
        ini = {'Comprobante':Ingreso.objects.get(pk=self.object.Comprobante.id)}            
        context['Numcomp'] = ini#['Comprobante']
        return context

    def get_success_url(self):
        #ppk = Ingreso_Conceptos.objects.get(pk=self.kwargs['pk'])
        #print('ppk',self.object.Comprobante.id)
        #url = reverse_lazy('ingreso_conceptos-list-view', kwargs={'pk':ppk.Comprobante.pk})
        url = reverse_lazy('ingreso-update-view', kwargs={'pk':self.object.Comprobante.id})
        return url

class IngresoConceptoCreateView(LoginRequiredMixin, CreateView):
    model = Ingreso_Conceptos
    
    form_class = IngresoConceptoForm 
    #template_name = "Comp/IngresoConcepto_create.html"
    template_name = "Comp/ingreso_conceptos_form_update2.html"
    
    def get_success_url(self):
        
        url = reverse_lazy('ingreso_conceptos-list-view', kwargs={'pk':self.kwargs['pk']})
        return url

    def get_context_data(self, **kwargs):
        context = super(IngresoConceptoCreateView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':  
            print('aaaaaaa', self)          
            ini = {'Comprobante':Ingreso.objects.get(pk=self.kwargs['pk'])}            
            
            context['form'] = IngresoConceptoForm(initial=ini)        
            context['Numcomp'] = ini#['Comprobante']
        return context

#Documentos relacionados
class CFDI_RelacionadoView(View):
    def get(self, request, *args, **kwargs):
        res = {}
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            id = request.GET.get('id', '') 
            print('iddd',id)
            if id != '':
                
                res = list(CfdiRelacionados_Ingreso.objects.values().filter(CFDI_Rel_id__Ingreso=id))
            
            return JsonResponse({'res':res}, safe=False, status=200)

        return JsonResponse({'res':res}, safe=False, status=500)


class Borra_CFDIRelacionadoView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print('Borrar',data['id'])
        try:
            obj = get_object_or_404(CfdiRelacionados_Ingreso, pk=data['id'])
            if obj:
                obj.delete()
                return JsonResponse({'res':True})
        except:
            return JsonResponse({'res':False})


class Add_CFDIRelacionadoView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print('Add', data)
        In = Ingreso.objects.get(Ingreso =data['id'])
        try:
            
            print( data['id'], data['UUID'], data['TR'])
        
            obj, created = CfdiRelacionados_Ingreso.objects.get_or_create(
                CFDI_Rel = In ,
                TipoRelacion = data['TR'],
                UUID = data['UUID']
            )
            print(obj, created)
            if created:            
                return JsonResponse({'res':True})  
            else:
                
                return JsonResponse({'res':False})
        except:            
            return JsonResponse({'res':False})

class Edit_CFDIRelacionadoView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        
        try:
            print("DR edit", data)
            obj = CfdiRelacionados_Ingreso.objects.get(pk=data['id'])
            
            if obj:
                
                obj.TipoRelacion = data['tr']
                obj.UUID =data['uuid']
                obj.save()
               
                return JsonResponse({'res':True})
        except:
            return JsonResponse({'res':False})
