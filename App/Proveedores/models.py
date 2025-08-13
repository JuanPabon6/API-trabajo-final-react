from django.db import models
from django.contrib.auth.models import User

class Proveedores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    IdProveedor = models.AutoField(primary_key=True)
    NameProveedor = models.TextField()
    EmailProveedor = models.TextField()
    PhoneProveedor = models.TextField()
    RoleProveedor = models.TextField()

    class Meta:
        db_table = 'Proveedores'

# Create your models here.
