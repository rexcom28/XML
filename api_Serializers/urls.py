from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views as rest_views



urlpatterns = [
    path('Ingreso/', views.IngresoDetail_ApiView.as_view(), name ='Ingreso_list'),
    path('Ingreso/<int:pk>', views.IngresoDetail_ApiView.as_view(), name ='Ingreso_detail'),
    path('Pago/', views.PagoDetail_ApiView.as_view(), name ='pago_list'),
    path('Pago/<int:pk>', views.PagoDetail_ApiView.as_view(), name ='pago_detail'),
]
