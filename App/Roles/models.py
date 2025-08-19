from django.db import models

class Roles(models.Model):
    IdRol = models.AutoField(primary_key=True)
    NameRol = models.TextField()

    class Meta:
        db_table = 'Roles'

# Create your models here.
