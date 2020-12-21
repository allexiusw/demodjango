from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(
        'Nombre', max_length=200, help_text="Texto de ayuda")
    quantity = models.IntegerField('Cantidad')
    price = models.FloatField('Precio')
    valid_date = models.DateField('Vencimiento')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name