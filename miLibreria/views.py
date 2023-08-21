from django.shortcuts import render
from .models import *
from django.http import HttpResponse,request
# Create your views here.

def listar_cliente(request):
    clientes = cliente.objects.all()
    resp=""
    for client in clientes:
        resp += f"{client.nombreCli}<br>"
    return HttpResponse(resp)


def inicio(request):
    return render(request,"inicio.html")

def clientes(request):
    return render(request,"clientes.html")

def libros(request):
    return render(request,"libros.html")