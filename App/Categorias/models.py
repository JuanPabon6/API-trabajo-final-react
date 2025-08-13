from django.db import models

class Categorias(models.Model):
    IdCategoria = models.IntegerField(primary_key=True)
    NameCategoria = models.TextField()

    class Meta:
        db_table = 'Categorias'

# Create your models here.
