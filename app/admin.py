from django.contrib import admin
from .models import cliente, producto, pedido

# Register your models here.

class clienteadmin(admin.ModelAdmin):
    list_display=["rut","nombre", "apellido", "direccion", "fono", "email"]
    list_editable=["fono", "email"]
    list_filter=["apellido", "rut"]
    search_fields=["rut", "nombre", "apellido" ]
    list_per_page= 5


class productoadmin(admin.ModelAdmin):
    list_display=["codigoproducto", "nombrep", "preciop"]
    list_editable=["preciop"]
    list_filter=["codigoproducto", "nombrep", "preciop"]
    search_fields=["codigoproducto", "nombrep", "preciop"]
    list_per_page = 5


class pedidoadmin(admin.ModelAdmin):    
    list_display=["numeropedido", "cliente", "producto", "entregado", "fecha"]
    list_editable=["entregado"]
    list_filter=["entregado", "fecha"]
    search_fields=["numeropedido", "cliente", "producto", "fecha"]
    list_per_page= 5 


admin.site.register(cliente, clienteadmin)
admin.site.register(producto, productoadmin)
admin.site.register(pedido, pedidoadmin)
