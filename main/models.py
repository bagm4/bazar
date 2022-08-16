from calendar import c
from distutils.command.upload import upload
import email
from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models
 
class Categoria (models.Model):
    nome = models.CharField(max_length=70)
    
    def __str__(self):
        return self.nome
    

class Produto (models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to='produto/', blank=True, null=True,max_length = 250)
    def __str__(self):
        return self.nome

# class Estado (models.Model):
#     nome = models.CharField(max_length=70)
#     sigla = models.CharField(max_length=2)
#     def __str__(self):
#         return self.nome

# class Cidade (models.Model):
#     nome = models.CharField(max_length=70)
#     cep = models.CharField(max_length=9)  
#     estado = models.ForeignKey(Estado, on_delete= models.CASCADE)
#     def __str__(self):
#         return self.nome

# class Endereco (models.Model):
#     cidade = models.OneToOneField(Cidade, on_delete=models.CASCADE)
#     bairro = models.CharField(max_length=70)
#     rua = models.CharField(max_length=100)
#     numero_casa = models.CharField(max_length= 5)
    
# class Cadastro_Usuario (models.Model):
#     nome = models.CharField(max_length=150)
#     cpf = models.CharField(max_length=12)
#     email = models.EmailField()
#     senha = models.CharField(max_length=100)
#     def __str__(self):
#         return self.nome

# class Login (models.Model):
#     email = models.EmailField()
#     senha = models.CharField(max_length=100)
#     def __str__(self):
#         return self.nome

# Create your models here.
