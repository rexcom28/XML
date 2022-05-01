from django.contrib import admin
from . models import *

admin.site.register(Pagos)
admin.site.register(DoctoRelacionado_Pagos)
admin.site.register(ImpuestoDR_Pagos)
admin.site.register(ImpuestoPago)
admin.site.register(ComprobantePagos)

