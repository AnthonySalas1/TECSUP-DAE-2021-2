from django.contrib import admin

# Register your models here.
from .models import Servicio, Categoria, Producto

admin.site.register(Servicio)
admin.site.register(Categoria)
admin.site.register(Producto)

