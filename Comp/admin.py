import site
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Ingreso)
admin.site.register(Ingreso_Conceptos)
admin.site.register(Impuesto_Ingreso)

admin.site.register(InformacionAduanera)

admin.site.register(CuentaPredial)
admin.site.register(Parte)
admin.site.register(Impuesto_PartidasIngreso)
admin.site.register(CfdiRelacionados_Ingreso)