from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    correo = forms.EmailField(max_length=200)

class TrabajadorForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=10)
    correo  = forms.EmailField(max_length=200)

class LibroForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=200)
    categoria = forms.CharField(max_length=100) 
    isbn = forms.CharField(max_length=50)
    #disponible = forms.BooleanField()

class RegistroUsuarioForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        help_texts = {campo:"" for campo in fields}