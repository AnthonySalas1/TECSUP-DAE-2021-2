from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()
    
    dicCategorias = {}
    for cat in category_list:
        dicCategorias[cat.id] = {
            'id' :cat.id,
            'nombre' : cat.nombre
        }

    request.session['nombreTienda'] = 'TIENDA TECH'
    request.session['category_list'] = dicCategorias
    
    context = { 
        'product_list': product_list,
    }
    return render(request, 'index.html', context)

def producto(request,producto_id):
    OBJproducto = Producto.objects.get(pk=producto_id)
    
    context = { 
        'producto': OBJproducto }
    return render(request, 'productos.html', context)

def indexByCategory(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    product_list = Producto.objects.filter( categoria = objCategoria)    
    category_list = Categoria.objects.all()
    context = { 
        'product_list': product_list
    }
    return render(request, 'index.html', context)

#######################
from tienda.carrito import Cart

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
