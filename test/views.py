from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calc
from .serializers import CalcSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello API!")