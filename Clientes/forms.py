import imp
from .models import Configuracion, Cliente, Producto
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ConfigEmpresaForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Configuracion
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))

class ClienteForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Cliente
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))    

class ProductoForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model  = Producto
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))