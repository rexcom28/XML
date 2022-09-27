from django.urls import path
from . views import (
    generate_csrf, 
    c_ClaveProdServView, 
    c_ClaveUnidadView,
    c_CodigoPostalView,
    c_FormaPagoView,
    c_TipoRelacionView
)
from . api_views import (
    c_FormaPago_APIListView,
    c_Moneda_APIListView,
    c_CodigoPostal_APIListView,
    c_RegimenFiscal_APIListView,
    c_Pais_APIListView,
    c_UsoCFDI_APIListView,
    c_ClaveProdServ_APIListView,
    c_ClaveUnidad_APIListView,
    c_Aduana_APIListView,
    c_PatenteAduanal_APIListView,
    c_Colonia_APIListView,
    c_Estado_APIListView,
    c_Localidad_APIListView,
    c_Municipio_APIListView,
    c_TipoRelacion_APIListView,
)

urlpatterns = [
    path('csrf/', generate_csrf),
    path('c_ClaveProdServView/',c_ClaveProdServView.as_view(), name='c_ClaveProdServ_list' ),
    path('c_ClaveUnidadView/',c_ClaveUnidadView.as_view(), name='c_ClaveUnidadView_list' ),
    path('c_CodigoPostalView/',c_CodigoPostalView.as_view(), name='c_CodigoPostalView_list' ),
    path('c_FormaPagoView/',c_FormaPagoView.as_view(), name='c_FormaPagoView_list' ),
    path('c_TipoRelacionView/',c_TipoRelacionView.as_view(), name='c_TipoRelacionView_list' ),    

    #API CALLS
    path('FormaPago/', c_FormaPago_APIListView.as_view() ),
    path('FormaPago/<FormaPago>/', c_FormaPago_APIListView.as_view() ),
    path('Moneda/', c_Moneda_APIListView.as_view() ),
    path('Moneda/<Moneda>/', c_Moneda_APIListView.as_view() ),
    path('CodigoPostal/', c_CodigoPostal_APIListView.as_view() ),
    path('CodigoPostal/<CodigoPostal>/', c_CodigoPostal_APIListView.as_view() ),
    path('Pais/',c_Pais_APIListView.as_view()),
    path('Pais/<Pais>/',c_Pais_APIListView.as_view()),
    path('Uso/',c_UsoCFDI_APIListView.as_view()),
    path('Uso/<Uso>/',c_UsoCFDI_APIListView.as_view()),
    path('Regimen/',c_RegimenFiscal_APIListView.as_view()),
    path('Regimen/<Regimen>/',c_RegimenFiscal_APIListView.as_view()),
    path('ProductoServ/',c_ClaveProdServ_APIListView.as_view()),
    path('ProductoServ/<ProductoServ>/',c_ClaveProdServ_APIListView.as_view()),
    path('ClaveUnidad/',     c_ClaveUnidad_APIListView.as_view()),
    path('ClaveUnidad/<ClaveUnidad>/',     c_ClaveUnidad_APIListView.as_view()),
    
    path('Aduana/',     c_Aduana_APIListView.as_view()),
    path('Aduana/<Aduana>/',     c_Aduana_APIListView.as_view()),

    path('PatenteAduanal/',     c_PatenteAduanal_APIListView.as_view()),
    path('PatenteAduanal/<PatenteAduanal>/',     c_PatenteAduanal_APIListView.as_view()),


    path('Colonia/',     c_Colonia_APIListView.as_view()),
    path('Colonia/<Colonia>/',     c_Colonia_APIListView.as_view()),

    path('Estado/',     c_Estado_APIListView.as_view()),
    path('Estado/<Estado>/',     c_Estado_APIListView.as_view()),

    path('Localidad/',     c_Localidad_APIListView.as_view()),
    path('Localidad/<Localidad>/',     c_Localidad_APIListView.as_view()),

    path('Municipio/',     c_Municipio_APIListView.as_view()),
    path('Municipio/<Municipio>/',     c_Municipio_APIListView.as_view()),

    path('TipoRelacion/',     c_TipoRelacion_APIListView.as_view()),
    path('TipoRelacion/<TipoRelacion>/',     c_TipoRelacion_APIListView.as_view()),





]