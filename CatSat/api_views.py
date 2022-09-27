from . models import *
from . serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
class ExamplePagination(PageNumberPagination):       
       page_size = 100


class c_FormaPago_APIListView(generics.ListAPIView):

    queryset = c_FormaPago.objects.all().order_by('FormaPago')
    serializer_class = c_FormaPago_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(FormaPago__icontains=self.kwargs['FormaPago'])
        else:
            return super().get_queryset()

class c_Moneda_APIListView(generics.ListAPIView):
    queryset = c_Moneda.objects.all().order_by('Moneda')
    serializer_class = c_Moneda_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Moneda__icontains=self.kwargs['Moneda'])
        else:
            return super().get_queryset()

class c_CodigoPostal_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_CodigoPostal.objects.all().order_by('CodigoPostal')
    serializer_class = c_CodigoPostal_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(CodigoPostal__icontains=self.kwargs['CodigoPostal'])
        else:
            return super().get_queryset()

class c_RegimenFiscal_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_RegimenFiscal.objects.all().order_by('Regimen')
    serializer_class = c_RegimenFiscal_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Regimen__icontains=self.kwargs['Regimen'])
        else:
            return super().get_queryset()

class c_Pais_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Pais.objects.all().order_by('Pais')
    serializer_class = c_Pais_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Pais__icontains=self.kwargs['Pais'])
        else:
            return super().get_queryset()

class c_UsoCFDI_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_UsoCFDI.objects.all().order_by('Uso')
    serializer_class = c_UsoCFDI_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Uso__icontains=self.kwargs['Uso'])
        else:
            return super().get_queryset()  

class c_ClaveProdServ_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_ClaveProdServ.objects.all().order_by('ProductoServ')
    serializer_class = c_ClaveProdServ_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(ProductoServ__icontains=self.kwargs['ProductoServ'])
        else:
            return super().get_queryset()  

class c_ClaveUnidad_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_ClaveUnidad.objects.all().order_by('ClaveUnidad')
    serializer_class = c_ClaveUnidad_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(ClaveUnidad__icontains=self.kwargs['ClaveUnidad'])
        else:
            return super().get_queryset() 

class c_Aduana_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Aduana.objects.all().order_by('Aduana')
    serializer_class = c_Aduana_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Aduana__icontains=self.kwargs['Aduana'])
        else:
            return super().get_queryset()

class c_PatenteAduanal_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_PatenteAduanal.objects.all().order_by('Patente')
    serializer_class = c_PatenteAduanal_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Patente__icontains=self.kwargs['Patente'])
        else:
            return super().get_queryset()

class c_Colonia_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Colonia.objects.all().order_by('Colonia')
    serializer_class = c_Colonia_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Colonia__icontains=self.kwargs['Colonia'])
        else:
            return super().get_queryset()

class c_Estado_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Estado.objects.all().order_by('Estado')
    serializer_class = c_Estado_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Estado__icontains=self.kwargs['Estado'])
        else:
            return super().get_queryset()

class c_Localidad_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Localidad.objects.all().order_by('Localidad')
    serializer_class = c_Localidad_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Localidad__icontains=self.kwargs['Localidad'])
        else:
            return super().get_queryset()
class c_Municipio_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_Municipio.objects.all().order_by('Municipio')
    serializer_class = c_Municipio_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Municipio__icontains=self.kwargs['Municipio'])
        else:
            return super().get_queryset()

class c_TipoRelacion_APIListView(generics.ListAPIView):
    pagination_class = ExamplePagination 
    queryset = c_TipoRelacion.objects.all().order_by('Relacion')
    serializer_class = c_TipoRelacion_Serializer
    def get_queryset(self, *args, **kwargs):
        if len(self.kwargs)!=0:
            return self.queryset.filter(Relacion__icontains=self.kwargs['Relacion'])
        else:
            return super().get_queryset()            