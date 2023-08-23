from django.contrib import admin
from .models import cliente,libro,trabajador,disponible

# Register your models here.

admin.site.register(libro)
admin.site.register(cliente)
admin.site.register(trabajador)
admin.site.register(disponible)