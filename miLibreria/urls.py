from django.urls import path
from .views import *

urlpatterns = [
    path('clientes_list/', listar_cliente),
    path('libreria/', inicio),
    path('libros/', libros),
    path('clientes/', clientes),
]
