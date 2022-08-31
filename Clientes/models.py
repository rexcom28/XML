from django.db import models
from CatSat.models import c_Pais,c_RegimenFiscal


class Cliente(models.Model):
    def c_paisC():
        return [(res.Pais, res.Pais+' - '+res.Descripcion) for res in c_Pais.objects.all()]
        
    def c_RegimenC():
        return [(reg.Regimen, reg.Regimen+' - '+reg.Descripcion) for reg in c_RegimenFiscal.objects.all()]
        
    
    clave   = models.CharField(max_length=8, unique=True)
    RFC     = models.CharField(max_length=13, unique=True)
    Nombre  = models.CharField(max_length=255)
    Regimen = models.CharField(max_length=3, choices=c_RegimenC())
    Domicilio   = models.CharField(max_length=5)
    Residencia  =models.CharField(max_length=3, choices=c_paisC(), default='MEX')
    Tax_id      = models.CharField(max_length=12, blank=True)
    Uso_CFDI    = models.CharField(max_length=3)

    def __str__(self):
        return self.RFC


class Configuracion(models.Model):
    def c_paisC():
        return [(res.Pais, res.Pais+' - '+res.Descripcion) for res in c_Pais.objects.all()]
        
    def c_RegimenC():
        return [(reg.Regimen, reg.Regimen+' - '+reg.Descripcion) for reg in c_RegimenFiscal.objects.all()]
        

    clave   = models.CharField(max_length=8, unique=True)
    RFC     = models.CharField(max_length=13, unique=True)
    Nombre  = models.CharField(max_length=255)
    Regimen = models.CharField(max_length=3, choices=c_RegimenC())
    Domicilio   = models.CharField(max_length=5)
    Recidencia  = models.CharField(max_length=3, default='MEX', choices=c_paisC())
    Num_Certificado = models.CharField(blank=True, null=True,max_length=55)
    IVA = models.DecimalField(null=True, max_digits=8, decimal_places=4)
    IVA_Ret = models.DecimalField(null=True, max_digits=8, decimal_places=4)
    ISR = models.DecimalField(null=True, max_digits=8, decimal_places=4)


    def __str__(self):
        return self.RFC

class Producto(models.Model):
    ClaveInterna  = models.CharField(max_length=10, unique=True)
    ClaveProducto = models.CharField(max_length=8)
    Descripcion   = models.CharField(max_length=255)
    Unidad        = models.CharField(max_length=5)
    ValorUnitario = models.DecimalField(null=True, max_digits=10, decimal_places=4)
    IVA           = models.BooleanField(default=False, blank=False, null=False)
    IVA_Ret       = models.BooleanField(default=False, blank=False, null=False)
    ISR           = models.BooleanField(default=False, blank=False, null=False)
    def __str__(self) -> str:
        return self.ClaveProducto+'-'+self.Descripcion

