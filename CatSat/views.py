from django.shortcuts import render
from django.views.generic import (
    View
)
from django.http import JsonResponse


from . models import *
from django.middleware.csrf import  get_token
from django.contrib.auth.decorators import login_required


def generate_csrf(request):
	return JsonResponse({'csrf_token': get_token(request)}, status=200)

class c_ClaveProdServView(View):
    def get(self, request,**kwargs):        
        ProdServ={}
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            fil = request.GET.get('prod', '')
            desc= request.GET.get('desc', '')            
            desc= False if desc =='false' or desc == '' else True
            print(fil,desc)
            
            if desc==False and str(fil)!='':
                ProdServ = list(c_ClaveProdServ.objects.values().filter(ProductoServ__startswith=str(fil))[:5000])
            elif desc==True:
                ProdServ = list(c_ClaveProdServ.objects.values().filter(Descripcion__startswith=fil)[:5000])                
        return JsonResponse({'ProdServ':ProdServ}, safe=False, status=200)        


class c_ClaveUnidadView(View):
    def get(self, request, *args, **kwargs):
        UniMedida=[]
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            UniMed = request.GET.get('UniMed', '')
            Desc_UniMed = request.GET.get('Desc_UniMed', '')            
            Desc_UniMed = False if Desc_UniMed =='false' or Desc_UniMed =='' else True
            print(Desc_UniMed, UniMed)
            if str(UniMed) !="":
                if not Desc_UniMed:
                    UniMedida = list(c_ClaveUnidad.objects.values().filter(ClaveUnidad__startswith=str(UniMed))[:5000])
                else:
                    UniMedida = list(c_ClaveUnidad.objects.values().filter(Nombre__startswith=str(UniMed))[:5000])
            else:
                UniMedida = list(c_ClaveUnidad.objects.values()[:5000])
        return JsonResponse({'UniMedida':UniMedida}, safe=False, status=200)
        

class c_CodigoPostalView(View):
    def get(self, request, *args, **kwargs):
        CodigoPostal = []
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            CoP = request.GET.get('CoP', '')
            
            Desc_CP      = request.GET.get('Desc_cp', '')
            
            Desc_CP      = False if Desc_CP == 'false' or Desc_CP == '' else True
            if CoP!='':
                if Desc_CP == False: 
                    CodigoPostal = list(c_CodigoPostal.objects.values().filter(CodigoPostal__startswith=CoP)[:500])
                else:
                    CodigoPostal = list(c_CodigoPostal.objects.values().filter(Estado_c__startswith=CoP)[:500])
            else:
                CodigoPostal = list(c_CodigoPostal.objects.values().filter()[:500])
        return JsonResponse({'CodigoPostal':CodigoPostal}, safe=False, status=200)
        

class c_FormaPagoView(View):
    def get(self,request, *args, **kwargs):
        FormaPago ={}
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            FormaPago = list(c_FormaPago.objects.values())
        return JsonResponse({'FormaPago':FormaPago}, safe=False, status=200)
        

class c_TipoRelacionView(View):
    def get(self, request, *args, **kwargs):
        TipoRel={}
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            TipoRel = list(c_TipoRelacion.objects.values())
        return JsonResponse({'TipoRel':TipoRel}, safe=False, status=200)
        