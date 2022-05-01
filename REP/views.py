
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    View,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComprobantePagos, Pagos, DoctoRelacionado_Pagos
from Comp.models import Ingreso
from Clientes.models import Configuracion
from .forms import  CompPagosForm, PagosFormSet,PagoForm, PagoAddDRForm
import datetime

from django.db.models import Count, Sum

def REPView(request):
    return HttpResponse('HOLA REP')

class ComprobantePagosListView(LoginRequiredMixin, ListView):
    model = ComprobantePagos
    template_name = 'REP/CompPagoList.html'


class ComprobantePagosCreateView(LoginRequiredMixin, CreateView):
    model = ComprobantePagos
    success_url = reverse_lazy('compPagos_list')    
    template_name = 'REP/CompPagosCreate.html'
    #form_class = CompPagosForm
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ComprobantePagosCreateView, self).get_context_data(**kwargs)
        
        if self.request.POST:            
            context['pago_inline_formset'] = PagosFormSet(self.request.POST)
        else:
            context['form'] = CompPagosForm(initial=self.get_Ini())
            context['pago_inline_formset'] = PagosFormSet()
        return context
    def get_Ini(self):
        
        try:
            Emi = Configuracion.objects.get(id=1)
            
            ini = {
                'Rfc_Emi':Emi.RFC,
                'Nombre_Emi':Emi.Nombre,
                'RegimenFiscal_Emi':Emi.Regimen,
                'NoCertificado':Emi.Num_Certificado,
                'Fecha': datetime.datetime.now()
            }   
        except:
            ini ={
                'Fecha': datetime.datetime.now()
            }
        return ini 
    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['pago_inline_formset']
        if formset.is_valid() and form.is_valid():
            response = super(ComprobantePagosCreateView, self).form_valid(form)
            form.save()            
            formset.instance=self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)

class ComprobantePagosUpdateView(LoginRequiredMixin, UpdateView):
    model = ComprobantePagos
    template_name = 'REP/CompPagosCreate.html'
    form_class = CompPagosForm
    success_url = reverse_lazy('compPagos_list')
    def get_context_data(self, **kwargs):
        context = super(ComprobantePagosUpdateView, self).get_context_data(**kwargs)
        context['qs']= Pagos.objects.filter(CompPago__id=self.kwargs['pk'])
        context['id']= self.kwargs['pk']
        return context
    
class ComprobantePagosDeleteView(LoginRequiredMixin, DeleteView):
    model = ComprobantePagos
    success_url = reverse_lazy('compPagos_list')

class PagosCreateView(LoginRequiredMixin, CreateView):
    model = Pagos
    form_class = PagoForm
    template_name = 'REP/pagosUpdate.html'
    def get_context_data(self, **kwargs):
        context = super(PagosCreateView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['idComp'] = self.kwargs['pk']  
            context['obj'] = self.object          
            #print("create", ComprobantePagos.objects.get(pk=self.kwargs['pk']))
            ini ={'CompPago': ComprobantePagos.objects.get(pk=self.kwargs['pk'])}
            context['form'] = PagoForm(initial=ini)
        return context
        
    def get_success_url(self):
        print('create pago', self.object.id)
        url = reverse_lazy('Pagos_update', kwargs={'pk':self.object.id})
        return url
class PagosUpdateView(LoginRequiredMixin, UpdateView):
    model = Pagos
    form_class = PagoForm
    template_name = 'REP/pagosUpdate.html'
    def get_context_data(self, **kwargs):
        context = super(PagosUpdateView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['idComp'] = self.object.CompPago.id
            context['obj'] = self.object
            context['DRs']= DoctoRelacionado_Pagos.objects.filter(Pago_rel__id=self.kwargs['pk'])            
            
            ini = {
                'Pago_rel':self.object
            }                       
            context['formDR']=PagoAddDRForm(initial=ini)
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            #print('req ', self.kwargs)
            res = {}
            try:
                DR = list(DoctoRelacionado_Pagos.objects.values().filter(id=self.kwargs['pk'] ))
                #print('DR', DR)
            except:
                return JsonResponse({'res':res}, safe=False, status=200)                        
            return JsonResponse({'res':DR}, safe=False, status=200)
        
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        url = reverse_lazy('Pagos_update', kwargs={'pk':self.object.id})
        return url

class PagosAddDRCreateView(LoginRequiredMixin, CreateView):
    model = DoctoRelacionado_Pagos
    template_name = 'REP/pagosAddDR.html'
    form_class = PagoAddDRForm
    def get_success_url(self):
        return reverse_lazy('Pagos_update', kwargs={'pk':self.kwargs['pk']})
    def get_context_data(self, **kwargs):
        context = super(PagosAddDRCreateView, self).get_context_data(**kwargs)
        if self.request.method =='GET':            
            ini = {'Pago_rel':Pagos.objects.get(pk=self.kwargs['pk']) }
            context['form']= PagoAddDRForm(initial=ini)
        return context

class PagoUpdateDRUpdateView(LoginRequiredMixin, UpdateView):
    model = DoctoRelacionado_Pagos
    form_class = PagoAddDRForm
    template_name = 'REP/pagosAddDR.html'
    
    def get_success_url(self):
        #print('OBJECT GOOD ',self.object.Pago_rel)
        #print('seuc', self.kwargs['pk'])
        return reverse_lazy('Pagos_update', kwargs={'pk':self.object.Pago_rel})


class PagosDR_ViewAPI(View):
    def get(self, request, *args, **kwargs):
        res = {}
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            id_pago = request.GET.get('id','')
            pago = Pagos.objects.get(id=id_pago)
            #print(pago.CompPago.Rfc_Rec)
            res = list(Ingreso.objects.values().filter(Rfc_Rec=pago.CompPago.Rfc_Rec))
        return JsonResponse({'res':res}, safe=False, status=200)


class Pagos_ChecarSaldo_ViewAPI(View):
    def get(self, request, *args, **kwargs):
        res = {}        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            id_ingreso = request.GET.get('id', '')
            pagoid = request.GET.get('pago', '')
            
            #ExistPago = DoctoRelacionado_Pagos.objects.filter(Pago_rel=pagoid, IdDocumento=id_ingreso)

            #verifica que el DR no este en el pago que esta por darse de alta al seleccionar el DR
            pag = DoctoRelacionado_Pagos.objects.filter(Pago_rel=pagoid, IdDocumento=id_ingreso).count()
            print('Existe pago',pag)
            if pag>0:
                return JsonResponse({'res':f'El docuemento relacionado ya esta dado de alta en este pago'}, safe=False, status=200)
            try:                
                #cuenta los pagos en los que el DR esta dado de alta que no sea el mismo pago 
                pag = DoctoRelacionado_Pagos.objects.filter(IdDocumento=id_ingreso).count()
                ing = Ingreso.objects.get(UUID=id_ingreso)
                
                if pag == 0:
                    res['NumParcialidad']= pag + 1
                    res['ImpSaldoAnt']  = ing.Total
                    res['ImpPagado']    = 0
                    res['ImpSaldoInsoluto'] = ing.Total
                else:
                    res = DoctoRelacionado_Pagos.objects.values('ImpSaldoAnt', 'ImpPagado', 'ImpSaldoInsoluto').filter(IdDocumento=id_ingreso).aggregate(
                        ImpSaldoAnt   = ing.Total - Sum('ImpSaldoAnt'),
                        ImpPagado     = ing.Total- Sum('ImpPagado'),
                        ImpSaldoInsoluto = ing.Total - Sum('ImpSaldoInsoluto')
                    )
                    res['NumParcialidad']= pag + 1
                    print('p: ',res)
            except:
                return JsonResponse({'res':f'error al intentar leer pago y/o ingreso'}, safe=False, status=200)
        return JsonResponse({'res':res}, safe=False, status=200)