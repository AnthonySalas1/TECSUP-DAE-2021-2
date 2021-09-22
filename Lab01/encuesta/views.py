from django.shortcuts import render
def index(request):
    context = {
    'titulo':'Formulario'
    }
    return render(request,"encuesta/formulario.html",context)



