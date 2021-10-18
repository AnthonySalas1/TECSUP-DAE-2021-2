from django.urls import path

from . import views

urlpatterns = [
    path('',views.serie_list),
    path('<int:pk>',views.serie_detail)

]