
from dataclasses import field
from pyexpat import model
from django.contrib import admin

from . models import *
from import_export import resources
from import_export.admin import ImportMixin

class c_FormaPago_CSV(resources.ModelResource):
    class Meta:
        model = c_FormaPago
        fields = ['id','FormaPago', 'Descripcion']

@admin.register(c_FormaPago)
class c_FormaPagoAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','FormaPago', 'Descripcion']
    resource_class = c_FormaPago_CSV
#------------

class c_Moneda_CSV(resources.ModelResource):
    class Meta:
        model = c_Moneda
        fields = ['id','Moneda','Descripcion']

@admin.register(c_Moneda)
class c_MonedaAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','Moneda','Descripcion']
    resources_class = c_Moneda_CSV
#--------------

class c_CodigoPostal_CSV(resources.ModelResource):
    class Meta:
        model = c_CodigoPostal
        fields = ['id','CodigoPostal','Estado_c', 'Municipio_c', 'Localidad_c']

@admin.register(c_CodigoPostal)
class c_CodigoPostalAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id','CodigoPostal','Estado_c', 'Municipio_c', 'Localidad_c']
        resources_class = c_CodigoPostal_CSV
#--------------------------------------------

class c_RegimenFiscal_CSV(resources.ModelResource):
    class Meta:
        model = c_RegimenFiscal
        fields = ['id', 'Regimen', 'Descripcion','Fisica','Moral']

@admin.register(c_RegimenFiscal)
class c_RegimenFiscalAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'Regimen', 'Descripcion','Fisica','Moral']
        resources_class = c_RegimenFiscal_CSV
#------------------------------------------------

class c_Pais_CSV(resources.ModelResource):
    class Meta:
        model = c_Pais
        fields = ['id', 'Pais', 'Descripcion']

@admin.register(c_Pais)
class c_PaisAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'Pais', 'Descripcion']
        resources_class = c_Pais_CSV
#-------------------------------------------------

class c_UsoCFDI_CSV(resources.ModelResource):
    class Meta:
        model = c_UsoCFDI
        fields = ['id', 'Uso', 'Descripcion']

@admin.register(c_UsoCFDI)
class c_UsoCFDIAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'Uso', 'Descripcion']
        resources_class = c_UsoCFDI_CSV
#-------------------------------------------------

class c_ClaveProdServ_CSV(resources.ModelResource):
    class Meta:
        model = c_ClaveProdServ
        fields = ['id', 'ProductoServ', 'Descripcion']
        
@admin.register(c_ClaveProdServ)
class c_UsoCFDIAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'ProductoServ', 'Descripcion']
        resources_class = c_ClaveProdServ_CSV
#-------------------------------------------------

class c_ClaveUnidad_CSV(resources.ModelResource):
    class Meta:
        model = c_ClaveUnidad
        fields = ['id', 'ClaveUnidad', 'Nombre','Descripcion']
        
@admin.register(c_ClaveUnidad)
class c_UsoCFDIAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'ClaveUnidad', 'Nombre','Descripcion']
        resources_class = c_ClaveUnidad_CSV
#-------------------------------------------------

class c_Aduana_CSV(resources.ModelResource):
    class Meta:
        model = c_Aduana
        fields = ['id', 'Aduana', 'Patente']
        
@admin.register(c_Aduana)
class c_AduanaAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'Aduana', 'Patente']
        resources_class = c_Aduana_CSV
#-------------------------------------------------

class c_PatenteAduanal_CSV(resources.ModelResource):
    class Meta:
        model = c_PatenteAduanal
        fields = ['id','Patente']
        
@admin.register(c_PatenteAduanal)
class c_PatenteAduanalAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id','Patente']
        resources_class = c_PatenteAduanal_CSV
#-------------------------------------------------

class c_Colonia_CSV(resources.ModelResource):
    class Meta:
        model = c_Colonia
        fields = ['id','Colonia', 'Codigo_c', 'NombreAsentamiento']
        
@admin.register(c_Colonia)
class c_PatenteAduanalAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id','Colonia', 'Codigo_c', 'NombreAsentamiento']
        resources_class = c_Colonia_CSV
#-------------------------------------------------

class c_Estado_CSV(resources.ModelResource):
    class Meta:
        model = c_Estado
        fields = ['id','Estado', 'Pais_c', 'Nombre_estado']
        
@admin.register(c_Estado)
class c_EstadoAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id','Estado', 'Pais_c', 'Nombre_estado']
        resources_class = c_Estado_CSV
#-------------------------------------------------

class c_TipoRelacion_CSV(resources.ModelResource):
     class Meta:
         model = c_TipoRelacion
         fields = ['id', 'Relacion', 'Descripcion']

@admin.register(c_TipoRelacion)
class c_c_TipoRelacionAdmin(ImportMixin, admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'Relacion', 'Descripcion']
        resources_class = c_TipoRelacion_CSV