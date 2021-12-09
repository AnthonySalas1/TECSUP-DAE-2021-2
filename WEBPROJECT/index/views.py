from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from index.controller import blueOn, greenOn, redOn , yellowOn, allOff
from django.shortcuts import render
from .models import Categoria, Producto
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home (request):
    return render (request, 'home.html')

def info (request):
    return render (request, 'infomatica.html')

def index_view (request):
    if request.POST:
        id = request.POST['id']
        if int(id) == 1:
            redOn()
        elif int(id) == 2:
            greenOn()
        elif int(id) == 3:
            blueOn()
        elif int(id) == 4:
            yellowOn()
        elif int(id) == 5:
            allOff()
        print(id)
    return render(request, 'homeduino.html')

def TCE(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()
    
    dicCategorias = {}
    for cat in category_list:
        dicCategorias[cat.id] = {
            'id' :cat.id,
            'nombre' : cat.nombre
        }
    request.session['nombrePagina'] = 'services categorias'
    request.session['category_list'] = dicCategorias
    
    context = { 
        'product_list': product_list,
    }
    return render(request, 'TCE.html', context)
    
def producto(request,producto_id):
    OBJproducto = Producto.objects.get(pk=producto_id)
    
    context = { 
        'producto': OBJproducto }
    return render(request, 'TCE.html', context)

def indexByCategory(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    product_list = Producto.objects.filter( categoria = objCategoria)    
    category_list = Categoria.objects.all()
    context = { 
        'product_list': product_list
    }
    return render(request, 'TCE.html', context)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def product_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductSerializer(producto, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        serie = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(serie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Producto.delete()
        return HttpResponse(status=204)