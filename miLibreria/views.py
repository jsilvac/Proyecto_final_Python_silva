from django.shortcuts import render
from . models import trabajador,cliente,libro
from django.http import HttpResponse
from .forms import ClienteForm,TrabajadorForm,LibroForm, RegistroUsuarioForm,RegistroUsuarioForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
    
def buscarXNombre(request):
    nombre = request.GET["nombre"]
    print(nombre)
    if nombre != "":
        lib = libro.objects.filter(nombreLi__icontains = nombre)
        return render(request,"resultadosbusqueda.html",{"libros":lib})
    else:
        return render(request,"busquedalibro.html", {"mensaje":"No me has ingresado nada"})

@login_required
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


class ClientesList(LoginRequiredMixin,ListView):
    model = cliente
    template_name = "clientes.html"

class ClientesCrear(LoginRequiredMixin,CreateView):
    model = cliente
    success_url = reverse_lazy("clientes_list")
    fields = ['nombreCli','correoCli']
    template_name = 'cliente_form.html'
 
class ClienteDetalle(LoginRequiredMixin,DetailView):
    model = cliente
    template_name = 'cliente_detalle.html'
     

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = cliente
    success_url = reverse_lazy("clientes_list")
    template_name = "cliente_confirm_delete.html"

class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model =cliente
    fields = ['nombreCli','correoCli']
    success_url = reverse_lazy("clientes_list")
    template_name = 'cliente_form.html'

@login_required
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
                
                mensaje="Libro agregado exitósamente"
                
            else:
                mensaje = "Datos no válidos"
                
        else: 
            mensaje = "Datos no válidos"

        formulario_libros = LibroForm()
        libros_list = libro.objects.all()
        return render(request,'libros.html', {"mensaje":mensaje, "formulario":formulario_libros, "libros": libros_list})
    else:
        formulario_libros = LibroForm()
        libros_list = libro.objects.all()
    return render(request,"libros.html", {"formulario":formulario_libros,"libros": libros_list})
    
@login_required
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
            mensaje = "Trabajador agregado exitósamente"
            return render(request,"trabajadores.html", {"mensaje":mensaje,"formulario": formulario_trabajador, "trabajador":trabajador_list})
        else:
            mensaje="Datos invalidos"
            return render(request, 'trabajadores.html',{"mensaje":mensaje})
    else:
        formulario_trabajador = TrabajadorForm()
    return render(request, 'trabajadores.html', {"formulario": formulario_trabajador} )


def disponible(request):
    return render(request,"disponible.html")

@login_required
def eliminarlibro(request,isbn):
    book = libro.objects.get(isbn=isbn)
    book.delete()
    mensaje="Libro eliminado"
    formulario_libros = LibroForm()
    libros_list = libro.objects.all()
    return render(request,'libros.html', {"mensaje":mensaje, "formulario":formulario_libros, "libros": libros_list})

@login_required
def editarlibro(request,isbn):
    book = libro.objects.get(isbn=isbn)
    print(isbn)
    if request.method == 'POST':
        form=LibroForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            book.nombreLi = info["nombre"]
            book.autorLi = info["autor"]
            book.categoriaLi = info["categoria"]
            book.isbn = info["isbn"] 
            # li = book(nombreLi=nombre, autorLi=autor, categoriaLi=categoria, isbn=isbn)
            book.save()
            
            mensaje="Libro editado exitósamente"
            formulario_libros = LibroForm()
            libros_list = libro.objects.all()
            return render(request,"libros.html", {"mensaje":mensaje,"formulario":formulario_libros,"libros": libros_list})
            
    else:  
        formulario_libros = LibroForm(initial={
            "isbn":book.isbn,
            "nombre":book.nombreLi,
            "autor":book.autorLi,
            "categoria":book.categoriaLi,
            "disponilbe":book.disponible,
        })
        return render(request,"editarlibro.html", {"formulario":formulario_libros, "libros":book})
    
def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info['username']
            pas=info["password"]
            print(usu +" "+pas)
            usuario=authenticate(username=usu, password=pas)    
            if usuario is not None:
                login(request, usuario)
                return render(request,"login.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request,"login.html", {"form":form,"mensaje":"Datos inválidos...!"})
        else:
             return render(request,"login.html", {"form":form,"mensaje":"Datos inválidos...!"})
    else:
        form= AuthenticationForm()
        return render(request,"login.html", {"form":form})
    
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            form.save()
            return render(request,"inicio.html",{"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"Datos iválidos...!"})
    else:
        form = RegistroUsuarioForm()
        return render(request, "register.html", {"form":form})
    
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.save()
            return render(request, "inicio.html",{"mensaje":f"Usuario {usuario.username} actualizado correctamente!"})
        else:
            return render(request, "editarPerfil.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Datos inválidos"})
    else:
        form=RegistroUsuarioForm(instance=usuario)    
        return render(request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username})


