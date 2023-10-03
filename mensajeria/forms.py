from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class messagesForm(forms.Form):
    message=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':40}))
    toUser=forms.ModelChoiceField(label="To",queryset=User.objects.all())
