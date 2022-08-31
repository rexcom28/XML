from . models import *
from django.db import models
from CatSat.models import c_FormaPago, c_TipoRelacion, c_UsoCFDI, c_RegimenFiscal, c_Pais

class Comprobante(models.Model):
    def c_Uso():
        return [(Uso.Uso, f'{Uso.Uso}-{Uso.Descripcion}') for Uso in c_UsoCFDI.objects.all()]
        
    def c_Regimen():
        return [(Reg.Regimen,f'{Reg.Regimen}-{Reg.Descripcion}') for Reg in c_RegimenFiscal.objects.all()]
        
    def c_Pais():
        return [(Pa.Pais,f'{Pa.Pais}-{Pa.Descripcion}') for Pa in c_Pais.objects.all()]
        

    NAP = '01'
    DEF = '02'
    TEM = '03'

    PUE = 'PUE'
    PPD = 'PPD'
    c_MetodoPago =(
        (PUE,'PUE-Pago en una sola exhibición'),
        (PPD,'PPD-Pago en parcialidades o diferido'),

    )
    c_Exportacion = (
        (NAP, '01-No aplica'),
        (DEF, '02-Definitiva'),
        (TEM, '03-Temporal'),
    )
    VIGENTE     = 'VIGENTE'
    ENVIADO     = 'ENVIADO'
    CANCELADO   = 'CANCELADO'
    TIMBRADO    = 'TIMBRADO'
    NUEVO       = 'NUEVO'
    MODIFICADO  = 'MODIFICADO'

    c_Estado = (
        (VIGENTE, 'VIGENTE'),
        (ENVIADO,'ENVIADO'),
        (CANCELADO, 'CANCELADO'),
        (TIMBRADO, 'TIMBRADO'),
        (NUEVO, 'NUEVO'),
        (MODIFICADO, 'MODIFICADO'),


    )

    def c_FormaPagoF():
        return [(FP.FormaPago, FP.FormaPago+'-'+FP.Descripcion) for FP in c_FormaPago.objects.all()]
        
    Version = models.CharField(max_length=5, default='4.0')
    Serie   = models.CharField(blank=True, max_length=25)
    Folio   = models.CharField(blank=True, max_length=40 )
    Fecha   = models.DateTimeField(blank=True)
    TipoCambio  = models.DecimalField(max_digits=10,decimal_places=6, blank=False, null=True)
    Moneda      = models.CharField(max_length=3, blank=False, default='MXN')    
    FormaPago   = models.CharField( choices=c_FormaPagoF(),max_length=2, blank=True, null=True)
    
    Exportacion = models.CharField(max_length=2, blank=False,null=False, choices=c_Exportacion, default=NAP)
    MetodoPago  = models.CharField(max_length=4, blank=True,null=True, choices=c_MetodoPago, default=PPD)
    LugarExpedicion = models.CharField(blank=False,null=False, max_length=5)

    TipoDeComprobante   = models.CharField(max_length=3, blank=False,null=False, default='I')
    NoCertificado   = models.CharField(max_length=20, blank=True)
    Certificado     = models.TextField(blank=True)
    Sello   = models.TextField(blank=True)

    SubTotal    = models.DecimalField(max_digits=21,decimal_places=6, blank=True, null=True)
    Descuento   = models.DecimalField(max_digits=11,decimal_places=6, blank=True, null=True)
    CondicionesDePago   = models.CharField(max_length=1000, blank=True, null=True)
    Total       = models.DecimalField(max_digits=21,decimal_places=6, blank=True, null=True)
    Confirmacion    = models.CharField(blank=True,null=True, max_length=5)

    created_at  = models.DateField(auto_now_add=True)
    Estado_CFDI = models.CharField(max_length=20, blank=True, default=NUEVO )

    IVA         = models.DecimalField(max_digits=18,decimal_places=6, blank=True, null=True)
    IVA_Ret     = models.DecimalField(max_digits=18,decimal_places=6, blank=True, null=True)
    ISR         = models.DecimalField(max_digits=18,decimal_places=6, blank=True, null=True)

    UUID        = models.CharField(max_length=36,blank=True, null=True, unique=True)

    class Meta:
        abstract  = True

class Emisor(models.Model):
    Rfc_Emi     = models.CharField( blank=False, max_length=15)
    Nombre_Emi  = models.CharField(blank=False, max_length=254)
    RegimenFiscal_Emi   = models.CharField(blank=False, max_length=4, choices= Comprobante.c_Regimen())
    FacAtrAdquirente_Emi = models.CharField(max_length=10, blank=True,null=True)
    class Meta:
        abstract = True

class Receptor(models.Model):
    Rfc_Rec     = models.CharField(blank=False, max_length=15)
    Nombre_Rec  = models.CharField(blank=False, max_length=254)
    RegimenFiscal_Rec   = models.CharField(blank=False, max_length=4, choices= Comprobante.c_Regimen())
    DomicilioFiscal_Rec     = models.CharField(blank=False, max_length=5)
    ResidenciaFiscal_Rec= models.CharField(max_length=3, default='MEX', choices=Comprobante.c_Pais(),null=False,blank=True)
    NumRegIdTrib_Rec    = models.CharField(max_length=40, blank=True, null=True)    
    UsoCFDI_Rec         = models.CharField(max_length=4, choices=Comprobante.c_Uso(),null=True,blank=True)
    
    class Meta:
        abstract = True

class ConceptoBase(models.Model):
    ClaveProdServ       = models.CharField(blank=False, max_length=8)
    NoIdentificacion    = models.CharField(blank=True, null=True, max_length=100)
    Cantidad            = models.DecimalField(blank=False, max_digits=15, decimal_places=6) 
    ClaveUnidad         = models.CharField(blank=False, max_length=4)
    Unidad              = models.CharField(blank=True, null=True,  max_length=20)
    Descripcion         = models.CharField(blank=True, max_length=1000)
    ValorUnitario       = models.DecimalField(blank=False, max_digits=18, decimal_places=6)
    Importe             = models.DecimalField(blank=True, max_digits=18, decimal_places=6)
    
    class Meta:
        abstract =True

class Concepto(ConceptoBase):  
    NoObj = '01'
    SiObj = '02'
    SiObj2= '03'
    c_ObjImp = (
        (NoObj,'01-No objeto de impuesto.'),
        (SiObj,'02-Sí objeto de impuesto.'),
        (SiObj2,'03-Sí objeto del impuesto y no obligado al desglose.'),
    )
    Descuento           = models.DecimalField(blank=True, null=True, max_digits=18, decimal_places=6)
    ObjetoImp           = models.CharField(blank=False, max_length=2, choices=c_ObjImp)
    
    class Meta: 
        abstract = True  

class CFDI_Relacionados_Base(models.Model):
    def c_Relacion():
        return [(rel.Relacion,rel.Relacion+'-'+rel.Descripcion) for rel in c_TipoRelacion.objects.all()]
        
    TipoRelacion    = models.CharField(max_length=2, choices=c_Relacion())
    UUID            = models.CharField(max_length=36, unique=True)
    class Meta:
        abstract =True

class ACuentaTerceros_Base(models.Model):    
    RfcACuentaTerceros      = models.CharField(blank=False, max_length=15)
    NombreACuentaTerceros   = models.CharField(blank=False, max_length=254)
    RegimenFiscalACuentaTerceros    = models.CharField(blank=False, max_length=3)
    DomicilioFiscalACuentaTerceros  = models.CharField(blank=False, max_length=5)        
    class Meta:
        abstract =True
class InformacionGlobal_Base(models.Model):
    Periodicidad    = models.CharField(blank=False, max_length=4)
    Meses           = models.CharField(blank=False, max_length=2)
    Año             = models.CharField(blank=False, max_length=4)
class Impuesto(models.Model):
    ISR = '001'
    IVA = '002'
    IEPS= '003'
    c_Impuestos = (
        (IVA, '002-IVA'),
        (ISR, '001-ISR'),
        (IEPS, '003-IEPS'),
    )
    TRASLADO ='TRASLADO'
    RETENCION='RETENCION'
    CHOICES =(
        (TRASLADO,'TRASLADO'),
        (RETENCION,'RETENCION'),
    )

    Base        = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=6)
    Impuesto    = models.CharField(blank=False, max_length=3, choices=c_Impuestos)
    TipoFactor  = models.CharField(blank=True, null=True, max_length=8)
    TasaOCuota  = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=6)
    Importe     = models.DecimalField(blank=True, null=True, max_digits=18, decimal_places=6)    
    Tipo_T_R            = models.CharField(blank=False, max_length=10, choices=CHOICES)

    class Meta:
        abstract = True




