from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from App.Clientes.models import Clientes
from App.Proveedores.models import Proveedores

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['is_superuser'] = self.user.is_superuser
        data['is_staff'] = self.user.is_staff

        try:
            cliente = Clientes.objects.get(user=self.user)
            data['role'] = 'cliente'
            data['cliente'] = {
                'id': cliente.IdCliente,
                'name': cliente.NameCliente,
                'email': cliente.EmailCliente,
                'phone': cliente.PhoneCliente
            }
            return data
        except Clientes.DoesNotExist:
            pass

        try:
            proveedor = Proveedores.objects.get(user=self.user)
            data['role'] = 'proveedor'
            data['proveedor'] = {
                'id': proveedor.IdProveedor,
                'name': proveedor.NameProveedor,
                'email': proveedor.EmailProveedor,
                'phone': proveedor.PhoneProveedor
            }
            return data
        except Proveedores.DoesNotExist:
            pass


        data['role'] = 'admin'
        return data