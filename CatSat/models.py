from django.db import models


class c_FormaPago(models.Model):
    FormaPago   = models.CharField(max_length=2, null=False,blank=False)
    Descripcion = models.CharField(max_length=50, null=False,blank=False)
    def __str__(self):
        return self.FormaPago+'-'+self.Descripcion
class c_Moneda(models.Model):
    Moneda  = models.CharField(max_length=3, null=False,blank=False)
    Descripcion = models.CharField(max_length=100, null=False,blank=False)
    def __str__(self):
        return self.Moneda+'-'+self.Descripcion
class c_CodigoPostal(models.Model):
    CodigoPostal= models.CharField(max_length=5, null=False,blank=False)
    Estado_c    = models.CharField(max_length=3, null=False,blank=False)
    Municipio_c = models.CharField(max_length=3, null=True,blank=True)
    Localidad_c = models.CharField(max_length=2, null=True,blank=True)
    def __str__(self):
        return self.CodigoPostal+'-'+self.Estado_c
class c_RegimenFiscal(models.Model):
    Regimen =models.CharField(max_length=3, null=False,blank=False)
    Descripcion = models.CharField(max_length=100, null=False,blank=False)
    Fisica  = models.BooleanField(null=True,blank=True)
    Moral   = models.BooleanField(null=True,blank=True)
    def __str__(self):
        return self.Regimen+'-'+self.Descripcion
class c_Pais(models.Model):
    Pais    = models.CharField(max_length=3, null=False,blank=False)
    Descripcion = models.CharField(max_length=65, null=False,blank=False)
    def __str__(self):
        return self.Pais
    

class c_UsoCFDI(models.Model):
    Uso = models.CharField(max_length=4, null=False,blank=False)
    Descripcion = models.CharField(max_length=65, null=False,blank=False)
    def __str__(self):
        return self.Uso+'-'+self.Descripcion
class  c_ClaveProdServ(models.Model):
    ProductoServ    = models.CharField(max_length=8, null=False,blank=False)
    Descripcion     = models.CharField(max_length=150, null=False,blank=False)
    def __str__(self):
        return self.ProductoServ+'-'+self.Descripcion
class c_ClaveUnidad(models.Model):
    ClaveUnidad = models.CharField(max_length=5, null=False,blank=False)
    Nombre      = models.CharField(max_length=150, null=False,blank=False)
    Descripcion = models.CharField(max_length=1000, null=False,blank=False)
    def __str__(self):
        return self.ClaveUnidad+'-'+self.Nombre+'-'+self.Descripcion
class c_Aduana(models.Model):
    Aduana  = models.CharField(max_length=3, null=False,blank=False)
    Patente = models.CharField(max_length=4, null=False,blank=False)
    def __str__(self):
        return self.Aduana+'-'+self.Patente
class c_PatenteAduanal(models.Model):
    Patente = models.CharField(max_length=4, null=False,blank=False)
    def __str__(self):
        return self.Patente
class c_Colonia(models.Model):
    Colonia     = models.CharField(max_length=5, null=False,blank=False)
    Codigo_c    = models.CharField(max_length=5, null=True,blank=True)
    NombreAsentamiento    = models.CharField(max_length=250, null=True,blank=True)
    def __str__(self):
        return self.Colonia+'- CP:'+self.Codigo_c+'-'+self.NombreAsentamiento
class c_Estado(models.Model):
    Estado  = models.CharField(max_length=4, null=False,blank=False)
    Pais_c  = models.CharField(max_length=3, null=True,blank=True)
    Nombre_estado =   models.CharField(max_length=100, null=True,blank=True)
    def __str__(self):
        return self.Estado+'-'+self.Nombre_estado
class c_Localidad(models.Model):
    Localidad = models.CharField(max_length=5, null=False,blank=False)
    Estado_c    = models.CharField(max_length=3, null=True,blank=True)
    Descripcion = models.CharField(max_length=150, null=True,blank=True)
    def __str__(self):
        return self.Localidad+'-'+self.Estado_c+', Desc: '+self.Descripcion
class c_Municipio(models.Model):
    Municipio   = models.CharField(max_length=4, null=False,blank=False)
    Estado_c    = models.CharField(max_length=3, null=True,blank=True)
    def __str__(self):
        return self.Municipio+'-'+self.Estado_c
class c_TipoRelacion(models.Model):
    Relacion = models.CharField(max_length=2, null=False,blank=False)
    Descripcion = models.CharField(max_length=150, null=True,blank=True)
    def __str__(self):
        return self.Relacion+'-'+self.Descripcion