from django.contrib import admin
from gestion_pedidos.models import Articulos,Clientes,Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')
    list_filter = ('nombre', 'direccion', 'telefono')

admin.site.register(Articulos)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos)
