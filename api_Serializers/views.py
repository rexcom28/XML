from urllib import response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Comp.models import *
from REP.models import *

from .serializers import * 
from .E_Tree import Create_XML as cXML

class IngresoDetail_ApiView(APIView):
    def get_object(self, pk):
        try:
            return Ingreso.objects.get(pk=pk)
        except Ingreso.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        
        if pk == None:
            ingresos = Ingreso.objects.all()
            serializer = Ingreso_Serializer(ingresos, many=True)
            return Response(serializer.data)
        comp = self.get_object(pk)
        serializer = Ingreso_Serializer(comp)
        #p = cXML(serializer.data,"ingreso")
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = Ingreso_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        ingreso = self.get_object(pk)        
        
        serializer = Ingreso_Serializer(ingreso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PagoDetail_ApiView(APIView):
    def get_object(self, pk):
        try:
            return ComprobantePagos.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        if pk==None:
            pagos = ComprobantePagos.objects.all()
            serializer = Pago_Serializer(pagos, many=True)
            return Response(serializer.data)

        pago  = self.get_object(pk)
        serializer = Pago_Serializer(pago)
        p = cXML(serializer.data, "pago")
        return Response(serializer.data)