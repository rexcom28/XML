from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *


class c_FormaPago_Serializer(serializers.ModelSerializer):
    class Meta:
        model = c_FormaPago
        fields = '__all__'
        ordering= 'FormaPago'


class c_Moneda_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_Moneda
        fields= '__all__'
        orderig = 'Moneda'

class c_CodigoPostal_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_CodigoPostal
        fields= '__all__'
        orderig = 'CodigoPostal'

class c_RegimenFiscal_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_RegimenFiscal
        fields= '__all__'
        orderig = 'Regimen'


class c_Pais_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_Pais
        fields= '__all__'
        orderig = 'Pais'


class c_UsoCFDI_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_UsoCFDI
        fields= '__all__'
        orderig = 'Uso'

class c_ClaveProdServ_Serializer(serializers.ModelSerializer):
    class Meta:
        model= c_ClaveProdServ
        fields= '__all__'
        orderig = 'ProductoServ'
