from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def login(request):
    response = {}
    response['result'] = 1
    response['message'] = ''
    data = request.data

    if data['username'] != "android" or data['password'] != "android":
        response['result'] = 0
        response['message'] = "Credenciales Inválidas"

    return Response(response)

