from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255) 
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-fecha_venta']
    
    def __str__(self):
        return self.nombre
    
    def total_producto(self):
        return f"{self.precio * self.cantidad}"
