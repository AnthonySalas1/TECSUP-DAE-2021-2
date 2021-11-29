from django.urls import path

from . import views

urlpatterns = [
    path('publico',views.publico),
    path('privado', views.privado)
]
