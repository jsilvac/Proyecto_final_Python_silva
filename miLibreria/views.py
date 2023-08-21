from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def listar_cliente(request):
    clientes = cliente.objects.all()
    resp=""
    for client in clientes:
        resp += f"{client.nombreCli}<br>"
    return HttpResponse(resp)
