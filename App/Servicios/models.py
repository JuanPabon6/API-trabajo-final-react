from django.db import models

class Servicios(models.Model):
    IdServicio = models.AutoField(primary_key=True)
    NameServicio = models.TextField()
    DescriptionServicio = models.TextField()
    PriceServicio = models.FloatField()

    class Meta:
        db_table = 'Servicios'

# Create your models here.
