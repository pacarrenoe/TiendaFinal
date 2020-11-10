from django.db import models

# Create your models here.

class cliente(models.Model):
    rut= models.CharField(max_length=9, verbose_name="Rut")
    nombre= models.CharField(max_length=20, verbose_name="Nombre")
    apellido= models.CharField(max_length=20, verbose_name="Apellido")
    direccion= models.CharField(max_length=40, verbose_name="Direccion")
    fono= models.IntegerField(verbose_name="Numero de contacto")
    email= models.EmailField(verbose_name="Email", null=False, blank=False)

    def datoscliente(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.nombre, self.apellido, self.rut)

    def __str__ (self):
        return self.datoscliente()

class producto(models.Model):
    codigoproducto= models.AutoField(primary_key=True, verbose_name="Numero de pedido")
    nombrep= models.CharField(max_length=35, verbose_name="Nombre del producto")
    preciop= models.IntegerField(verbose_name="Precio")
    descripcion= models.TextField(max_length=500, blank=True, null=True, verbose_name="Descripcion")
    imagen= models.ImageField(upload_to="productos", null=True)

    def __str__ (self):
        return self.nombrep     
    
class pedido(models.Model):
    numeropedido= models.AutoField(primary_key=True, verbose_name="Numero de pedido")    
    cliente= models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Cliente")
    producto= models.ForeignKey(producto, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Producto")
    entregado= models.BooleanField(verbose_name="Entregado")
    fecha= models.DateTimeField(verbose_name="Fecha de pedido")


    def final(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.cliente, self.numeropedido, self.entregado)

    def __str__ (self):
        return self.final()    
                          
