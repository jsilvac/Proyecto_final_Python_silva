from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('clientes_list/', listar_cliente),
    path('libreria/', inicio, name="inicio"),
    path('libros/', libros, name= "libros"),
    path('clientes/', clientes, name = "clientes"),
    path('trabajadores/', trabajadores, name = "trabajadores"),
    path('disponible/', disponible, name = "disponible"),
    path('busquedalibro/', busquedalibro, name="busquedalibro"),
    path('buscar/', buscar, name="buscar"),
    path('buscarxnombre/', buscarXNombre, name="buscarXNombre"),
    path('eliminarlibro/<isbn>', eliminarlibro, name="eliminarlibro"),
    path('editarlibro/<isbn>', editarlibro , name="editarlibro"),
    path('clientes/list/', ClientesList.as_view(), name="clientes_list"),
    path('clientes/new/', ClientesCrear.as_view(), name="clientes_crea"),
    path('clientes/<pk>', ClienteDetalle.as_view(), name="cliente_detalle"),
    path('clientes/delete/<pk>', ClienteDelete.as_view(), name="cliente_delete"),
    path('clientes/update/<pk>', ClienteUpdate.as_view(), name="cliente_update"),
    
    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]

 