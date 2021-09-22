from django.contrib import admin

# Register your models here.
from . models import Categoria
from . models import Producto
from . models import Cliente


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)

