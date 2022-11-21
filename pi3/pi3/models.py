from django.db import models
from datetime import date

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, primary_key=True)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=9)
    comp_cep = models.CharField(max_length=200)
    def __str__(self):
        return self.cpf

class Multa(models.Model):
    data_desbloqueio = models.DateField()
    cpf_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
        
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Livro(models.Model):
    isbn = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    data_aquisicao = models.DateField()
    estado = models.CharField(max_length=200)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    cpf_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_livro = models.OneToOneField(Livro, on_delete=models.CASCADE, primary_key = True)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()