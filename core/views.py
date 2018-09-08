from django.shortcuts import render
from catalogo.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html') 

def contato(request):
    return render(request, 'contato.html')


