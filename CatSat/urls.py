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
    c_CodigoPostal_APIListView
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


]