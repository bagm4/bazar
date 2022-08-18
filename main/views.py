from multiprocessing import context
from django.shortcuts import render

from .models import Produto
#from django.http import HttpResponse

# Create your views here.

def index (request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render (request, 'index.html', context)

def detalhes (request, id):
    produto = Produto.objects.get(id=id)
    context = {'produto' : produto}
    return render (request, 'detalhe.html', context)

def quem_somos (request):
    return render (request, 'quem_somos.html')

def feminino (request):
    context = {'categoria': 'feminino'}
    Produto.objects.filter(categoria__nome='feminino')
    return render(request, 'classe.html', context) 

def masculino (request):
    context = {'categoria': 'masculino'}
    return render(request, 'classe.html', context) 

def acessorios (request):
    context = {'categoria': 'acessorios'}
    return render(request, 'classe.html', context) 

def ofertas (request):
    context = {'categoria': 'ofertas'}
    return render(request, 'classe.html', context) 


def quem_somos (request):
    context = {'categoria': 'quem_somos'}
    return render(request, 'quem_somos.html', context) 
