from ast import arg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import (
    View,
    CreateView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Cliente, Configuracion, Producto
from .forms import ConfigEmpresaForm, ClienteForm, ProductoForm
from django.urls import reverse_lazy

class c_ClientesView(View):
    def get(self, request,**kwargs):
        RFC = request.GET.get('RFC', '').upper()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            Clientes = list(Cliente.objects.values().filter(RFC__startswith=str(RFC)))        
            return JsonResponse({'Clientes':Clientes}, safe=False, status=200)
        return render(request, 'Ingreso.html')

class c_ProductosView(View):
    def get(self, request, **kargs):
        ClaveInterna = request.GET.get('clvaI','')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            Productos = list(Producto.objects.values().filter(ClaveInterna__startswith=ClaveInterna))
            return JsonResponse({'Productos': Productos}, safe=False, status=200)
        #return render(request, 'Ingreso.html')
        return JsonResponse({'Productos': {}}, safe=False, status=500)
        
class ConfiguracionEmpresaView(LoginRequiredMixin, UpdateView):
    model = Configuracion
    template_name = "Clientes/ConfigEmpresa_form.html"
    form_class = ConfigEmpresaForm
    success_url  =  reverse_lazy('ingreso-list-view')
    def get(self, request, *args,**kwargs):
        obj, created = Configuracion.objects.get_or_create(pk=self.kwargs['pk'])
        print ('obj ', obj, '   ', 'crea', created)
        return super().get(self, request, *args, **kwargs)

#Cliente---------------
class ClientesListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "Clientes/lista_clientes.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "Clientes/Cliente_from.html"
    form_class = ClienteForm
    success_url  =  reverse_lazy('cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model= Cliente

    def post(self, request, *args, **kwargs):        
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self):
        url = reverse_lazy('cliente_list')
        return url

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "Clientes/Cliente_from.html"
    form_class = ClienteForm
    def get_success_url(self):
        url = reverse_lazy('cliente_list')
        return url

#Producto------
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'Clientes/productos_list.html'
    
class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'Clientes/Productos_form.html'
    form_class   = ProductoForm
    def get_success_url(self):
        url = reverse_lazy('items_list')
        return url 

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url  =  reverse_lazy('items_list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'Clientes/Productos_form.html'
    form_class   = ProductoForm
    success_url  =  reverse_lazy('items_list')