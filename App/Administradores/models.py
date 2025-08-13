from django.db import models
from django.contrib.auth.models import User

class Administradores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    IdAdmin = models.AutoField(primary_key=True)
    NameAdmin = models.TextField()
    EmailAdmin = models.TextField()
    PhoneAdmin = models.TextField()
    RoleAdmin = models.TextField()

    class Meta:
        db_table = 'Administradores'

# Create your models here.
