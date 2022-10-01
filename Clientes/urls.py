from django.urls import path

from . import api_views
from .views import (
    c_ClientesView, 
    c_ProductosView,
    ConfiguracionEmpresaView, 
    ClienteCreateView, 
    ClientesListView, 
    ClienteDeleteView, 
    ClienteUpdateView,
    ProductoCreateView,
    ProductoListView,
    ProductoUpdateView,
    ProductoDeleteView,
    )

urlpatterns =[
    path('c_ClientesView/',c_ClientesView.as_view(), name='c_Clientes_list' ),
    path('c_ProductosView/', c_ProductosView.as_view(), name='c_Productos_list'),
    path('ConfigEmpresa/<pk>/',ConfiguracionEmpresaView.as_view(), name='configuracionEmpresa' ),
    path('ClienteCreate/',ClienteCreateView.as_view(), name='cliente_create' ),
    path('Cliente/<pk>/Update/',ClienteUpdateView.as_view(), name='cliente_update' ),
    path('',ClientesListView.as_view(), name='cliente_list' ),
    path('Clientes/delete/<pk>/cliente/',ClienteDeleteView.as_view(), name='delete_cliente' ),
    path('ProductoCreate/',ProductoCreateView.as_view(), name='create_items' ),
    path('ProductoList/',ProductoListView.as_view(), name='items_list' ),
    path('Producto/<pk>/update/',ProductoUpdateView.as_view(), name='items_update' ),
    path('<pk>/delete/', ProductoDeleteView.as_view(), name='items_delete'),

    # api cliente login/logoue
    path('login/', api_views.LoginView.as_view()),
    path('logout/', api_views.LogoutView.as_view()),

    path('profile/', api_views.ProfileView.as_view()),
]