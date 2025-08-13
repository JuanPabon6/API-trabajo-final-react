from django.urls import path, include

urlpatterns = [
    path('Administradores/', include('App.Administradores.urls')),
    path('Categorias/', include('App.Categorias.urls')),
    path('Clientes/', include('App.Clientes.urls')),
    path('Productos/', include('App.Productos.urls')),
    path('Proveedores/', include('App.Proveedores.urls')),
    path('Roles/', include('App.Roles.urls')),
    path('Servicios/', include('App.Servicios.urls')),
    path('login/', include('App.Login.urls'))
]