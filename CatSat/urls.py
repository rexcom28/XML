from django.urls import path
from . views import (
    generate_csrf, 
    c_ClaveProdServView, 
    c_ClaveUnidadView,
    c_CodigoPostalView,
    c_FormaPagoView,
    c_TipoRelacionView
)

urlpatterns = [
    path('csrf/', generate_csrf),
    path('c_ClaveProdServView/',c_ClaveProdServView.as_view(), name='c_ClaveProdServ_list' ),
    path('c_ClaveUnidadView/',c_ClaveUnidadView.as_view(), name='c_ClaveUnidadView_list' ),
    path('c_CodigoPostalView/',c_CodigoPostalView.as_view(), name='c_CodigoPostalView_list' ),
    path('c_FormaPagoView/',c_FormaPagoView.as_view(), name='c_FormaPagoView_list' ),
    path('c_TipoRelacionView/',c_TipoRelacionView.as_view(), name='c_TipoRelacionView_list' ),

    
]