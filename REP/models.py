
from django.db import models
from CatSat.models import c_FormaPago
from Comp.models import Ingreso
from Clientes.models import Configuracion
from Comp.models_Abst import (
    Impuesto,
    Comprobante,
    Emisor,
    Receptor,
    CFDI_Relacionados_Base,
)

from django.core.validators import MinLengthValidator

class ComprobantePagos(Comprobante,Emisor,Receptor):
    #override fields from Comprobante
    NumPago             = models.CharField(max_length=10, blank=False, null=False, unique=True)    
    FormaPago           = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)
    TipoDeComprobante   = models.CharField(max_length=3, blank=False, null=False, default='P')
    CondicionesDePago   = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)
    SubTotal            = models.DecimalField(max_digits=1,decimal_places=1, default=0, editable=False, blank=True, null=True)
    Descuento           = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)
    Moneda              = models.CharField(max_length=3, default='XXX', editable=False, null=True,blank=True)
    TipoCambio          = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)
    Total               = models.DecimalField(max_digits=1,decimal_places=1, default=0, editable=False, blank=True, null=True)
    Exportacion         = models.CharField(max_length=2, blank=False,null=False, choices=Comprobante.c_Exportacion,default=Comprobante.NAP)
    MetodoPago          = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)

    #emisor Override
    FacAtrAdquirente    = models.CharField(max_length=2, default='NA', editable=False, null=True,blank=True)
    UsoCFDI_Rec         = models.CharField(max_length=4, default='CP01', choices=Comprobante.c_Uso(),null=True,blank=True)
    def __str__(self):
        return f'Pago: {self.NumPago}'

class CfdiRelacionados_REP(CFDI_Relacionados_Base):
    CFDI_Rel        = models.ForeignKey(ComprobantePagos, related_name='CFDI_REL_REP', on_delete=models.CASCADE)
    def __str__(self):
        return f'Numero REP: {self.CFDI_Rel.NumPago}, UUID: {self.UUID}'

class Pagos(models.Model):
    def c_FormaPagoF():
        return [(FP.FormaPago, FP.FormaPago+'-'+FP.Descripcion) for FP in c_FormaPago.objects.all()]
        
    CompPago        = models.ForeignKey(ComprobantePagos, related_name='Pagos_Rep',on_delete=models.CASCADE, blank=True, null=True)

    FechaPago       = models.DateTimeField(blank=False)

    FormaDePagoP    = models.CharField( choices=c_FormaPagoF(),max_length=2, blank=False, null=False)
    
    MonedaP         = models.CharField(max_length=3, blank=False, default='MXN')
    TipoCambioP     = models.DecimalField(max_digits=18,decimal_places=6, blank=False, null=True)
    Monto           = models.DecimalField(max_digits=18,decimal_places=6, blank=False, null=True)
    #NumOperacion
    RfcEmisorCtaOrd = models.CharField(max_length=13,blank=True, validators=[MinLengthValidator(12)])
    NomBancoOrdExt  = models.CharField(max_length=100,blank=True)
    CtaOrdenante    = models.CharField(max_length=50,blank=True )
    RfcEmisorCtaBen = models.CharField(max_length=13,blank=True, validators=[MinLengthValidator(12)] )
    CtaBeneficiario = models.CharField(max_length=50,blank=True, validators=[MinLengthValidator(10)] )
    #TipoCadPago     = 
    #CertPago        = 
    #CadPago
    #SelloPago
    def __str__(self):
        return f'{str(self.id)}'

class DoctoRelacionado_Pagos(models.Model):
    NoObj = '01'
    SiObj = '02'
    SiObj2= '03'
    c_ObjImp = (
        (NoObj,'01-No objeto de impuesto.'),
        (SiObj,'02-Sí objeto de impuesto.'),
        (SiObj2,'03-Sí objeto del impuesto y no obligado al desglose.'),
    )

    Pago_rel        = models.ForeignKey(Pagos, related_name='Pagos_DR',on_delete=models.CASCADE)
    IdDocumento     = models.CharField(max_length=36,blank=False, validators=[MinLengthValidator(36)])
    Serie           = models.CharField(max_length=25,blank=True, validators=[MinLengthValidator(1)])
    Folio           = models.CharField(max_length=40,blank=True, validators=[MinLengthValidator(1)])
    MonedaDR        = models.CharField(max_length=3,blank=False)
    EquivalenciaDR  = models.DecimalField(max_digits=11,decimal_places=6, blank=True, null=True)
    NumParcialidad  = models.IntegerField()
    ImpSaldoAnt     = models.DecimalField(max_digits=18,decimal_places=6, blank=False, null=True)
    ImpPagado       = models.DecimalField(max_digits=18,decimal_places=6, blank=False, null=True)
    ImpSaldoInsoluto= models.DecimalField(max_digits=18,decimal_places=6, blank=False, null=True)
    ObjetoImp       = models.CharField(blank=False, max_length=2, default='02',choices=c_ObjImp)

    def Make_DRs_Impuestos(self):
        
        try:
            ingreso= Ingreso.objects.get(UUID= self.IdDocumento )
            iva = True if ingreso.IVA > 0 else False
            iva_ret = True if ingreso.IVA_Ret > 0 else False
            isr = True if ingreso.ISR > 0 else False
            impuestos = list(Configuracion.objects.values('IVA', 'IVA_Ret', 'ISR'))
            #print(impuestos[0]['IVA'])
            IMPS = {'IVA':[iva, impuestos[0]['IVA']/100], 'IVA_Ret':[iva_ret,impuestos[0]['IVA_Ret']/100],'ISR':[isr, impuestos[0]['ISR']/100]}
            for key, value in IMPS.items():
                if value[0]:
                    #print(key, value[0], value[1])
                    obj, created = ImpuestoDR_Pagos.objects.get_or_create(
                        docto_rel = self,
                        Impuesto = '002' if key == 'IVA' else ( '002' if key=='IVA_Ret' else '001'),
                        Tipo_T_R = 'TRASLADO' if key == 'IVA' else ( 'RETENCION' if key=='IVA_Ret' else 'RETENCION')
                    )
                    
                    if obj:
                        obj.Base = self.ImpPagado
                        obj.TipoFactor = 'Tasa'
                        obj.TasaOCuota =  value[1]
                        obj.Importe =  self.ImpPagado * value[1]
                        obj.save()
                    

                    #print(f'obj: {obj}, created:{created}')

        except:
            pass        


    def save(self, *args, **kwargs):
        super(DoctoRelacionado_Pagos, self).save(*args, **kwargs)
        self.Make_DRs_Impuestos()

    def __str__(self):
        return f'{str(self.id)}-{self.Pago_rel}-UUID:{self.IdDocumento}'


class ImpuestoDR_Pagos(Impuesto):
    docto_rel = models.ForeignKey(DoctoRelacionado_Pagos, related_name='DR_Pagos_Impuestos',on_delete=models.CASCADE)
    def __str__(self):
        return f'{str(self.id)}-{self.docto_rel}'
class ImpuestoPago(Impuesto):
    Pago_rel    = models.ForeignKey(Pagos, on_delete=models.CASCADE)
    def __str__(self):
        return f'{str(self.id)}-{self.Pago_rel}'