from django.db import models

class Categorias(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    NameCategoria = models.TextField()

    class Meta:
        db_table = 'Categorias'

# Create your models here.
