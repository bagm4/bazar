"""bazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Feminino/', feminino, name='feminino'),
    path('masculino/', masculino, name='masculino'),
    path('acessorios/', acessorios, name='acessorios'),
<<<<<<< HEAD
    path('quem_somos/', quem_somos, name='quem_somos'),
=======
    path('detalhes/<int:id>', detalhes, name='detalhes'),
>>>>>>> 7ee1b2a71051306241683f0e15a1b65a040bb7ca
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
