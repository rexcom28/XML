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

