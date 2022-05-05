



from . models import Parte, Ingreso, Ingreso_Conceptos

from django import forms
from django.forms import BaseInlineFormSet, ValidationError, inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from CatSat.models import c_ClaveProdServ

class ParteForm(forms.ModelForm):

    class Meta:
        exclude =['Ingreso_Concepto','InfoAduanera']
        model = Parte
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))

    helper.form_method ='POST'

#Encabezado
class IngresoForm(forms.ModelForm):
    
    Fecha = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        

        fields = '__all__'
        labels={
            'LugarExpedicion':('C.P.:'),
        }
        model   = Ingreso
        # widgets={
        #     'Nombre_Rec':forms.TextInput(attrs={'v-model':'Nombre_Rec', }),
        #     'RegimenFiscal_Rec':forms.TextInput(attrs={'v-model':'RegimenFiscal_Rec', }),
        #     'DomicilioFiscal_Rec':forms.TextInput(attrs={'v-model':'DomicilioFiscal_Rec', }),
        #     'ResidenciaFiscal_Rec':forms.TextInput(attrs={'v-model':'ResidenciaFiscal_Rec', }),
        #     'NumRegIdTrib_Rec':forms.TextInput(attrs={'v-model':'NumRegIdTrib_Rec', }),
        #     'UsoCFDI_Rec':forms.TextInput(attrs={'v-model':'UsoCFDI_Rec', }),
        # }
        
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))

#Partidas
class IngresoConceptoForm(forms.ModelForm):
    
    class Meta:
        #exclude =['NoIdentificacion', 'InfoAduanera']
        model = Ingreso_Conceptos
        fields ='__all__'
        
        labels={
            'Comprobante':(''),
            'ClaveProdServ':('Producto Servicio'),
            'ClaveUnidad':('Clave Unidad'),
            'ValorUnitatrio':('Valor Unitario'),
            'ObjetoImp':('Objeto Impuesto'),
        }
        widgets= {
            'Comprobante': forms.Select(attrs={
                # 'placeholder': 'Rol ...',
                'class': 'input-group-field',
                'required': True,
                'style':'display:none',
                }),
            
            
            
        } 
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class='btn btn-primary mt-2'))

class MyformSet(BaseInlineFormSet):    
    def clean(self):
        super().clean()
        for form in self.forms:            
            if form.cleaned_data:

                err = 0
                strErr  = ''
                print(form.cleaned_data)

                if 'ValorUnitario' in form.cleaned_data and 'Cantidad' in form.cleaned_data:
                    if 'Descuento' in form.cleaned_data :
                        form.instance.Importe = form.cleaned_data['Cantidad'] * form.cleaned_data['ValorUnitario'] 
                        des = form.cleaned_data.get('Descuento') if not  form.cleaned_data.get('Descuento')  == None else 0
                        if des > form.instance.Importe :
                            err +=1
                            strErr +=f'-El descuento ${ form.cleaned_data["Descuento"] }  asignado es mayor al importe ${ form.cleaned_data["Importe"]}\n'                

                if 'ObjetoImp' not in form.cleaned_data :                    
                    #raise forms.ValidationError(f'El campo Objeto Impuesto no puede estar Vacío')
                    err +=1
                    strErr +='El campo Objeto Impuesto no puede estar Vacío\n'
                if 'ClaveProdServ' not in form.cleaned_data:
                    err +=1
                    strErr +='El campo Clave Producto/Servicio Vacío \n\r'
                else:
                    Prod = c_ClaveProdServ.objects.values().filter(ProductoServ=form.cleaned_data.get('ClaveProdServ'))                    
                    if len(Prod) <= 0 and form.cleaned_data.get('ClaveProdServ') not in Prod:
                        raise forms.ValidationError(f'El campo Clave Producto/Servicio no existe en el catálogo')

                if 'NoIdentificacion' not in form.cleaned_data or form.cleaned_data.get('NoIdentificacion')=='' :
                    err +=1
                    strErr +='El campo Numero Identificacion esta vacío\n'

                if 'Cantidad' not in form.cleaned_data or form.cleaned_data.get('Cantidad')=='':
                    err +=1
                    strErr +='El campo Cantidad no puede ser 0 \n'
                if 'ClaveUnidad' not in form.cleaned_data or form.cleaned_data.get('ClaveUnidad')=='':
                    err +=1
                    strErr +='La Clave Unidad no puede estar vacía \n'
                if 'Unidad' not in form.cleaned_data or form.cleaned_data.get('Unidad')=='':
                    err +=1
                    strErr +='La Unidad no puede estar vacía \n'

                if 'Descripcion' not in form.cleaned_data or form.cleaned_data.get('Descripcion')=='':
                    err +=1
                    strErr +='La Descripcion no puede estar vacío \n'

                if 'ValorUnitario' not in form.cleaned_data or form.cleaned_data.get('ValorUnitario')=='':
                    err +=1
                    strErr +='El valor unitario no puede ser 0 \n'

                if err >0:
                    raise ValidationError(strErr)
        return form.cleaned_data


IngresoFomSet = inlineformset_factory(
    Ingreso,     
    Ingreso_Conceptos,
    
    extra=2,
    fields=[
        
        'Comprobante',
        'Descuento',
        'ObjetoImp',
        'ClaveProdServ',
        'NoIdentificacion',
        'Cantidad',
        'ClaveUnidad',
        'Unidad',
        'Descripcion',
        'ValorUnitario',
        'Importe',
        'IVA',
        'ISR',
        'IVA_Ret'
    ], 
    #exclude= [ ],
    formset=MyformSet
    


 )    