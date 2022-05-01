import imp
from django.urls import path
from .views import *
urlpatterns =[
    path('Rep/', REPView, name='rep_view'),
    path('CompPagos/', ComprobantePagosListView.as_view(), name='compPagos_list'),
    path('compPagos/create/', ComprobantePagosCreateView.as_view(), name='compPagos_create'),
    path('compPagos/update/<pk>/', ComprobantePagosUpdateView.as_view(), name='compPagos_update'),
    path('CompPagos/delete/<pk>/', ComprobantePagosDeleteView.as_view(), name='compPagos_delete'),
    path('compPagos/updatePago/<pk>/', PagosUpdateView.as_view(), name='Pagos_update'),
    path('compPagos/createPago/<pk>/', PagosCreateView.as_view(), name='Pagos_create'),
    path('compPagos/addDRPago/<pk>/', PagosAddDRCreateView.as_view(), name='PagosAddDR_create'),
    path('compPagos/updateDRPago/<pk>/', PagoUpdateDRUpdateView.as_view(), name='PagoDR_update'),    
    path('compPagos/seekdrPago/', PagosDR_ViewAPI.as_view(), name='PagosDR_api'),
    path('compPagos/checarSaldoPago/', Pagos_ChecarSaldo_ViewAPI.as_view(), name='PagosChecarSaldo_api'),
    

    
]