from django.shortcuts import render
from .models import *
# Create your views here.

def lista_produtos(request):
    contexto = {
        'lista_produtos': Produto.objects.all()
    }
    return render(request, 'lista_produtos.html', contexto)

def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    contexto = {
        'categoria_corrente': categoria,
        'lista_produtos': Produto.objects.filter(categoria=categoria),
    }
    return render(request, 'categoria.html', contexto)

def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto': produto,
    }
    return render(request, 'produto.html', contexto)