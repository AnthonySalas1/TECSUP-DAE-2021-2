from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'index'

urlpatterns = [

    ##Inicio de la pagina
    path('', views.home, name='home')
    ,

    ##Control de la Iluminación de una casa
    path('homeduino', views.index_view, name = 'homeduino')
    ,
    
    ##Espacio de noticias
    path('infomatica',views.info, name = 'infomatica')
    ,

    ##Tienda de Componenetes
    path('TCE', views.TCE, name = 'TCE'),
    path('producto', views.producto, name='producto')
    ,
    path('categoria/<int:categoria_id>',views.indexByCategory,name='categoria'),
    ##API
    path('api/list',views.product_list),
    path('api/detail/<int:pk>',views.product_detail)
]

