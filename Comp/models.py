

import decimal


from django.forms import ValidationError

from . models_Abst import (

    Comprobante,
    Emisor,
    Receptor,
    ConceptoBase,
    Concepto,
    CFDI_Relacionados_Base,
    ACuentaTerceros_Base,
    InformacionGlobal_Base,
    Impuesto,
    
)
from Clientes.models import Configuracion

from django.db import models
from django.urls.base import reverse
from django.db.models import Sum 




class InformacionAduanera(models.Model):    
    NumeroPedimento     = models.CharField(blank=False, max_length=21, unique=True)
    def __str__(self) :
        return self.NumeroPedimento

class Ingreso(Comprobante,Emisor,Receptor):
    Ingreso     = models.CharField(max_length=10, blank=False, null=False, unique=True)

    UsoCFDI_Rec         = models.CharField(max_length=4, choices=Comprobante.c_Uso(),null=True,blank=True)
    def __str__(self):
        return self.Ingreso
    def save(self, *args, **kwargs):
        
        if self.Estado_CFDI !=self.TIMBRADO and self.id != None :
            self.Estado_CFDI=self.MODIFICADO
            
        #run the save Perform action after database operation
        super(Ingreso, self).save(*args, **kwargs)
        
        #so the inlines partidas are in the DB to sumarize TAXES
        self.Zuma()
        super(Ingreso, self).save(*args, **kwargs)
        

        
    def Zuma(self):        
        # imp = Ingreso_Conceptos.objects.filter(Comprobante=self.id).aggregate(
        #     Total_Importe= Sum('Importe'),
            
        #     Tot_Descuento = Sum('Descuento')
        # )
        IVA= decimal.Decimal(0.0000)
        IVA_R = decimal.Decimal(0.0000)
        ISR = decimal.Decimal(0.0000)
        for i in Impuesto_PartidasIngreso.objects.filter(Imp_Partida__Comprobante=self.id):
            if i.Impuesto == i.IVA and i.Tipo_T_R==i.TRASLADO:
                IVA     += decimal.Decimal(i.Importe)
            if i.Impuesto == i.IVA and i.Tipo_T_R==i.RETENCION:
                IVA_R += decimal.Decimal(i.Importe)
            if i.Impuesto== i.ISR:
                ISR += decimal.Decimal(i.Importe)

        self.IVA = IVA
        self.IVA_Ret = IVA_R
        self.ISR = ISR
        try:
            self.Total = (self.SubTotal - self.Descuento) + (self.IVA+self.ISR)-self.IVA_Ret
        except:
            self.Total = 0    
        #print(f'Importes partidas{IVA}--- {i.TRASLADO}  {i.id} {i.Impuesto},  Tipo_T_R:{i.Tipo_T_R}, Imp{i.Importe}')
                    
        
        
class Impuesto_Ingreso(Impuesto):
    
    ImpuestosIngreso    = models.ForeignKey(Ingreso, related_name='Impuestos_Ingreso', on_delete=models.CASCADE)
          
class Ingreso_Conceptos(Concepto):
    Comprobante      = models.ForeignKey(Ingreso, on_delete=models.CASCADE, null=False)
    #InfoAduanera    = models.ManyToManyField(InformacionAduanera, related_name='Concepto_InfoAduana', blank=True)
    IVA= models.BooleanField(default=False, blank=False, null=False)
    ISR= models.BooleanField(default=False, blank=False, null=False)
    IVA_Ret= models.BooleanField(default=False, blank=False, null=False)

    def Loop_ins_atts(self):
        imp = list(Configuracion.objects.values('IVA', 'IVA_Ret', 'ISR'))
        iva = imp[0]['IVA']/100
        ivar= imp[0]['IVA_Ret']/100
        isr = imp[0]['ISR']/100

        for attribute, value in self.__dict__.items():
            if attribute in ['IVA','ISR', 'IVA_Ret'] and value:
                #print('TRUE: ', attribute, '=', value)
                obj, created = Impuesto_PartidasIngreso.objects.get_or_create(
                    Imp_Partida_id  = self.id,
                    Impuesto        = '002' if attribute in ['IVA_Ret','IVA'] else '001',
                    Tipo_T_R        = 'RETENCION' if attribute=='IVA_Ret' else ( 'RETENCION' if attribute=='ISR' else 'TRASLADO')
                )
                if obj:
                    obj.Base = self.Importe
                    obj.TipoFactor= 'Tasa'
                    obj.TasaOCuota = iva if attribute=='IVA' else (ivar if attribute=='IVA_Ret' else isr)
                    obj.Importe = self.Importe * decimal.Decimal(obj.TasaOCuota)
                    obj.save()
            elif attribute in ['IVA','ISR', 'IVA_Ret'] and value==False:
                #print('FALSE: ', attribute, '=', value)
                try:
                    obj = Impuesto_PartidasIngreso.objects.get(
                        Imp_Partida_id = self.id,
                        Impuesto ='002' if attribute in ['IVA_Ret','IVA'] else '001',
                        Tipo_T_R ='RETENCION' if attribute=='IVA_Ret' else 'TRASLADO'
                    )
                    if obj:
                        obj.delete()
                except :
                    pass

    def save(self, *args, **kwargs):        
        self.Importe = (self.ValorUnitario * self.Cantidad ) - self.Descuento        
        super(Ingreso_Conceptos, self).save(*args, **kwargs)
        self.Loop_ins_atts()

    def __str__(self):
        return f'{self.Comprobante}- {self.id}'

class Impuesto_PartidasIngreso(Impuesto):
    Imp_Partida = models.ForeignKey(Ingreso_Conceptos, on_delete=models.CASCADE)
    def __str__(self):
        return f'Comp: {self.Imp_Partida.Comprobante}, -Impuesto({self.Impuesto}),   ${self.Importe}'

class CuentaPredial(models.Model):
    Ingreso_Concepto    = models.ForeignKey(Ingreso_Conceptos, related_name='IngresoConcepto_CtaPredial', on_delete=models.CASCADE)
    Numero      = models.CharField(blank=False, max_length=150)


class Parte(ConceptoBase):
    Ingreso_Concepto     = models.ForeignKey(Ingreso_Conceptos, related_name='IngresoConcepto_Parte', on_delete=models.CASCADE, blank=True, null=True)
    InfoAduanera    = models.ManyToManyField(InformacionAduanera, related_name='Parte_InfoAduana', blank=True)
    def __str__(self):
        return str(self.Descripcion)
    

class ACuentaTerceros_Ingreso(ACuentaTerceros_Base):
    Ingreso_Concepto         = models.ForeignKey(Ingreso_Conceptos, related_name='Ingreso_Concepto_ACT', on_delete=models.CASCADE)
    
class InformacionGlobal_Ingreso(InformacionGlobal_Base):
    Ingreso_InfoGlo     = models.ForeignKey(Ingreso, related_name='Ingreso_InfoGlobal', on_delete=models.CASCADE)
    

class CfdiRelacionados_Ingreso(CFDI_Relacionados_Base):
    CFDI_Rel        = models.ForeignKey(Ingreso, related_name='CFDI_REL_Comprobante', on_delete=models.CASCADE)
    def __str__(self):
        return self.CFDI_Rel.Ingreso+', UUID: '+self.UUID
    



