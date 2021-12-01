from rest_framework import serializers
from rest_framework .decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
@api_view(['GET'])
def producto_list(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)