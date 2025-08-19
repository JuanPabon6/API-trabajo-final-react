from django.db import models
from App.Categorias.models import Categorias

class Producto(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    NameProducto = models.TextField()
    PriceProducto = models.FloatField()
    CategoryId = models.ForeignKey(Categorias, on_delete=models.CASCADE, default=1)
    ImageUrl = models.TextField()

    class Meta:
        db_table = 'Productos'

# Create your models here.
