from django.db import models

class Producto(models.Model):
    IdProducto = models.IntegerField(primary_key=True)
    NameProducto = models.TextField()
    PriceProducto = models.FloatField()
    # CategoryId = models.ForeignKey()
    ImageUrl = models.TextField()

    class Meta:
        db_table = 'Productos'

# Create your models here.
