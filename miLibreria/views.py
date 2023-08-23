from django.shortcuts import render
from . models import trabajador,cliente,libro
from django.http import HttpResponse
from .forms import ClienteForm,TrabajadorForm,LibroForm
# Create your views here.

def listar_cliente(request):
    clientes = cliente.objects.all()
    resp=""
    for client in clientes:
        resp += f"{client.nombreCli}<br>"
    return HttpResponse(resp)

def listar_libros(request):
    libros = libro.objects.all()
    res=""
    for libro in libros:
        res+= f"{libro.nombre}<br>"
    return HttpResponse(res)

def inicio(request):
    return render(request,"inicio.html")

def busquedalibro(request):
    return render(request,"busquedalibro.html")

def buscar(request):
    isbn=request.GET["isbn"]
    
    if isbn != "":
        xlibros = libro.objects.filter(isbn__icontains=isbn)
        print(xlibros)
        return render(request,"resultadosbusqueda.html",{"libros":xlibros})
    else:
        return render(request,"busquedalibro.html", {"mensaje":"no me ingresaste nada"})

def clientes(request):
    if request.method == "POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            correo=info["correo"]
            cli = cliente(nombreCli=nombre,correoCli=correo)
            cli.save()
            clientes_list = cliente.objects.all()
            formulario_cliente = ClienteForm()   
            return render(request,"clientes.html", {"mensaje":"Cliente agregado exitósamente","formulario":formulario_cliente, "clientes":clientes_list})     
        else:
            return render(request,"clientes.html", {"mensaje":"Datos inválidos"})
    else:
        formulario_cliente = ClienteForm()
    return render(request,"clientes.html", {"formulario" : formulario_cliente})

def libros(request):
    if request.method =='POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            if info["nombre"] :
                nombre = info["nombre"]
                autor = info["autor"]
                categoria = info["categoria"]
                isbn = info["isbn"] 
                li = libro(nombreLi=nombre, autorLi=autor, categoriaLi=categoria, isbn=isbn)
                li.save()
                formulario_libros = LibroForm()
                libros_list = libro.objects.all()
                return render(request,'libros.html', {"mensaje":"Libro agregado exitósamente", "formulario":formulario_libros, "libros": libros_list})
            else:
                return render(request,"libros.html", {"formulario":formulario_libros})
        else:
            return render(request,'libros.html',{"mensaje":"Datos inválidos"})
    else:
        formulario_libros = LibroForm()
    return render(request,"libros.html", {"formulario":formulario_libros})
    

def trabajadores(request):
    if request.method =='POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            telefono=info["telefono"]
            correo=info["correo"]
            trabj = trabajador(nombreTrabj=nombre, telefonoTraj=telefono, corrreoTrabj=correo)
            trabj.save()
            trabajador_list = trabajador.objects.all()
            formulario_trabajador = TrabajadorForm()
            return render(request,"trabajadores.html", {"mensaje":"Trabajador agregado exitósamente","formulario": formulario_trabajador, "trabajador":trabajador_list})
        else:
            return render(request, 'trabajadores.html',{"mensaje":"Datos invalidos"})
    else:
        formulario_trabajador = TrabajadorForm()
    return render(request, 'trabajadores.html', {"formulario": formulario_trabajador} )


def disponible(request):
    return render(request,"disponible.html")