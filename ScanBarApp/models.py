from django.db import models

# Create your models here.

class Barcode(models.Model):
    sku = models.CharField(max_length=200)
    sap = models.CharField(max_length=8, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField(default=0)
    codigo_barras = models.CharField(max_length=100, unique=False)
    #Aqui esta variable de base de datos vamos a poder almacenar las imagenes del producto
    #imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  #este campo es para relacionar el producto con una imagen
