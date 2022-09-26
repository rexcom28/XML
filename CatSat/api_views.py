from . models import *
from . serializers import *
from rest_framework import generics

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