from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def publico(request):
    data = {
        'mensaje':'acceso publico'
        }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def privado(request):
    data = {
        'mensaje':'acceso privado'
        }
    return Response(data)
