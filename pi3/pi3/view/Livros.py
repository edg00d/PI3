from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Livro_form(ModelForm):
    class Meta:
        model= Livro
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super(Livro_form, self).__init__(*args, **kwargs)
        self.fields['editora'].empty_label = 'Selecione uma Editora'
        self.fields['autor'].empty_label = 'Selecione um Autor'

def lista(request):
    return render(request, 'Livros/lista.html', {
        'Livros': Livro.objects.all()
    })
def lista_livros(request):
    return render(request, 'Livros/lista_livros.html', {
        'Livros': Livro.objects.all()
    })
def lista_disp(request):
    return render(request, 'Livros/lista_disp.html', {
        'Livros': Livro.objects.exclude(status = False)
    })
def novo(request):
    frm = Livro_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Livros.lista')
    return render(request, 'Livros/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Livro'
    })
def editar(request, id):
    livro = get_object_or_404(Livro, pk=id)
    frm = Livro_form(request.POST or None, instance= livro)
    if frm.is_valid():
        frm.save()
        return redirect('Livros.lista')
    return render(request, 'Livros/form.html',{
        'frm':frm,
        'titulo': 'Editar Livro'
    })
def excluir(request, id):
    livro = get_object_or_404(Livro, pk=id)
    frm = Livro_form(request.POST or None, instance= livro)
    livro.delete()
    return redirect('Livros.lista')