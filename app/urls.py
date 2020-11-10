from django.urls import path, include
from .views import home, menu, nosotros, pedidos, usuario, usuario_listado, usuario_nuevo, usuario_modificar, usuario_eliminar, registrar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('menu/', menu, name="menu"),
    path('nosotros/', nosotros, name="nosotros"),
    path('pedido/', pedidos, name="pedido"),
    path('usuario/', usuario, name="usuario"),
    path('usuario_listado/', usuario_listado, name="usuario_listado"),
    path('usuario_nuevo/', usuario_nuevo, name="usuario_nuevo"),
    path('usuario_modificar/<codigoproducto>/', usuario_modificar, name="usuario_modificar"),
    path('usuario_eliminar/<codigoproducto>/', usuario_eliminar, name="usuario_eliminar"),
    path('registrar_usuario/', registrar_usuario, name="registrar_usuario"),

    
]