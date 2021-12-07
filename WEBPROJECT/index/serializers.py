from rest_framework import serializers
from .models import Categoria, Producto, Servicio



class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Categoria
      fields = 'nombre'

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
      model = Producto
      fields = '__all__'
      depth = 1
