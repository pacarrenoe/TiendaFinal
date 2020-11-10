from django.shortcuts import render, redirect
from .models import cliente, producto, pedido
from .forms import productosForm

# Create your views here.

def home(request):

    return render(request, 'app/home.html')

def menu(request):

    return render(request, 'app/menu.html')

def nosotros(request):

    return render(request, 'app/nosotros.html')

def pedidos(request):

    return render(request, 'app/pedido.html')

def usuario(request):

    return render(request, 'app/usuario.html') 

def usuario_listado(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'app/usuario_listado.html', data)         

def usuario_nuevo(request):
    data = {
        'form':productosForm()
    }

    if request.method =='POST':
        formulario = productosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se ha creado un nuevo producto"

    return render(request, 'app/usuario_nuevo.html', data) 

def usuario_modificar(request, codigoproducto):
    productos= producto.objects.get(codigoproducto=codigoproducto)
    data = {
        'form':productosForm(instance=producto)
    }

    if request.method =='POST':
        formulario = productosForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se ha modificado el producto"
            data['form'] = formulario

    return render(request, 'app/usuario_modificar.html', data) 

def usuario_eliminar(request, codigoproducto):
    productos= producto.objects.get(codigoproducto=codigoproducto)
    productos.delete()
    
    return redirect(to='usuario_listado') 





    