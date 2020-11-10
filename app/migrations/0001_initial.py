# Generated by Django 3.1.3 on 2020-11-08 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('direccion', models.CharField(max_length=40, verbose_name='Direccion')),
                ('fono', models.IntegerField(verbose_name='Numero de contacto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigoproducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de pedido')),
                ('nombrep', models.CharField(max_length=35, verbose_name='Nombre del producto')),
                ('preciop', models.IntegerField(verbose_name='Precio')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripcion')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('numeropedido', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de pedido')),
                ('entregado', models.BooleanField(verbose_name='Entregado')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de pedido')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente', verbose_name='Cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto', verbose_name='Producto')),
            ],
        ),
    ]