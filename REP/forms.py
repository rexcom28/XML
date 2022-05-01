from django.forms import BaseInlineFormSet, ValidationError, inlineformset_factory
from .models import ComprobantePagos,Pagos,DoctoRelacionado_Pagos
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CompPagosForm(forms.ModelForm):
    Fecha = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        fields= '__all__'
        model = ComprobantePagos
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-primary mt-2'))

class PagoForm(forms.ModelForm):
    FechaPago = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Pagos
        fields = '__all__'
        labels={
            'CompPago':(''),
        }
        wigets={
            'CompPago':forms.Select(attrs={
                
                'class': 'input-group-field',
                'required': True,
                'style':'display:none',
                }),
        }
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))
PagosFormSet = inlineformset_factory(
    ComprobantePagos,
    Pagos,
    extra=1,
    fields=[
        'CompPago',
        'FechaPago',
        'FormaDePagoP',
        'MonedaP',
        'TipoCambioP',
        'Monto',       
    ]
)


class PagoAddDRForm(forms.ModelForm):
    class Meta:
        
        model = DoctoRelacionado_Pagos
        fields= '__all__'
        wigets={
            'Pago_rel':forms.Select(attrs={
                
                'class': 'input-group-field',
                'required': True,
                'style':'display:none',
                }),
        }
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-primary mt-2'))