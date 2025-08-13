from django.db import models
from django.contrib.auth.models import User

class Clientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    IdCliente = models.IntegerField(primary_key=True)
    NameCliente = models.TextField()
    EmailCliente = models.TextField()
    PhoneCliente = models.TextField()
    RoleCliente = models.TextField()

    class Meta:
        db_table = 'Clientes'

# Create your models here.
