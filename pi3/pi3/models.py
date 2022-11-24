from django.db import models
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, primary_key=True)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=9)
    comp_cep = models.CharField(max_length=200)
    status = models.BooleanField(default = True)
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
    data_aquisicao = models.DateField(auto_now_add = True)
    estado = models.CharField(max_length=200)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    status = models.BooleanField(default = True)
    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    cpf_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_previ_dev = models.DateField()