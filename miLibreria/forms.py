from django import forms

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