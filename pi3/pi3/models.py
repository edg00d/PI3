from tkinter import CASCADE
from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, primary_key=True)
    senha = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=9)
    comp_cep = models.CharField(max_length=200)

class multa(models.Model):
    data_desbloqueio = models.DateField()

class editora(models.Model):
    nome = models.CharField(max_length=200)
    
class autor(models.Model):
    nome = models.CharField(max_length=200)
    bio = models.CharField(max_length=400)

class livro(models.Model):
    isbn = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    data_aquisicao = models.DateField()
    estado = models.CharField(max_length=200)
    situacao_livro = models.BooleanField(null=True)
    editora = models.ForeignKey('editora', on_delete=models.CASCADE)
    autor = models.ForeignKey('autor', on_delete=models.CASCADE)
