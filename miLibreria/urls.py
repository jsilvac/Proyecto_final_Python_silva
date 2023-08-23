from django.urls import path
from .views import *

urlpatterns = [
    path('clientes_list/', listar_cliente),
    path('libreria/', inicio, name="inicio"),
    path('libros/', libros, name= "libros"),
    path('clientes/', clientes, name = "clientes"),
    path('trabajadores/', trabajadores, name = "trabajadores"),
    path('disponible/', disponible, name = "disponible"),
    path('busquedalibro/', busquedalibro, name="busquedalibro"),
    path('buscar/', buscar, name="buscar"),
]
 