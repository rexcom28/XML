
from django.urls import path
from .views import (
    index, ParteCreateView, 
    IngresoListView, IngresoCreateView, 
    IngresoConceptos_ListView, 
    ConceptoUpdateView, 
    IngresoConceptoCreateView, 
    IngresoUpdateView, 
    DeleteIngresoView, 
    CFDI_RelacionadoView,
    Borra_CFDIRelacionadoView,
    Add_CFDIRelacionadoView,
    Edit_CFDIRelacionadoView,
)

urlpatterns = [
    #path('', index, name='index'),
    path('parte/create/' , ParteCreateView.as_view(), name='parte-create-view'),    
    path('' , IngresoListView.as_view(), name='ingreso-list-view'),
    path('ingreso/create/' , IngresoCreateView.as_view(), name='ingreso-create-view'),
    path('ingreso_conceptos/<pk>/list/' , IngresoConceptos_ListView.as_view(), name='ingreso_conceptos-list-view'),
    path('ingreso/<pk>/update/' , ConceptoUpdateView.as_view(), name='ingreso-concepto-update-view'),
    path('ingreso_m/<pk>/update/' , IngresoUpdateView.as_view(), name='ingreso-update-view'),    
    path('ingreso_concepto/<pk>/create/' , IngresoConceptoCreateView.as_view(), name='ingreso_concepto-create-view'),
    path('delete/<pk>/ingreso/', DeleteIngresoView.as_view(), name="delete_ingreso"),
    path('doctoRelacion/', CFDI_RelacionadoView.as_view(), name='doctRelacion_view'),
    path('doctoRelacion_delete/', Borra_CFDIRelacionadoView.as_view(), name='borra_doctRelacion_view'),
    path('doctoRelacion_add/', Add_CFDIRelacionadoView.as_view(), name='add_doctRelacion_view'),
    path('doctoRelacion_edit/', Edit_CFDIRelacionadoView.as_view(), name='edit_doctRelacion_view'),

    
]