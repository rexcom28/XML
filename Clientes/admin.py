from django.contrib import admin
from .models import Cliente, Configuracion, Producto
admin.site.register(Cliente)
admin.site.register(Configuracion)
admin.site.register(Producto)
