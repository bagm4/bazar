from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index (request):
    return render (request, 'index.html')

def feminino (request):
    context = {'categoria': 'feminino'}
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



