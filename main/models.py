from calendar import c
import email
from django.db import models

class subcategoria (models.Model):
    nome = models.CharField(max_length=70)
 
class Categoria (models.Model):
    nome = models.CharField(max_length=70)
    #subcategoria
 
 
class Produto (models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()
    #categoria
    #subcategoria
  

class Estado (models.Model):
    nome = models.CharField(max_length=70)
    sigla = models.CharField(max_length=2)

class Cidade (models.Model):
    nome = models.CharField(max_length=70)
    cep = models.CharField(max_length=9)  
    estado = models.ForeignKey(Estado, on_delete= models.CASCADE)

class Endereco (models.Model):
    cidade = models.OneToOneField(Cidade, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=70)
    rua = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length= 5)




class Usuario (models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    #endereço


# Create your models here.
