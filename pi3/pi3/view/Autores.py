from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Autor_form(ModelForm):
    class Meta:
        model= Autor
        fields= '__all__'
def lista(request):
    return render(request, 'Autores/lista.html', {
        'Autores': Autor.objects.all()
    })
def novo(request):
    frm = Autor_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Autores.lista')
    return render(request, 'Autores/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Autor'
    })
def editar(request, id):
    autor = get_object_or_404(Autor, pk=id)
    frm = Autor_form(request.POST or None, instance= autor)
    if frm.is_valid():
        frm.save()
        return redirect('Autores.lista')
    return render(request, 'Autores/form.html', {
        'frm': frm,
        'titulo': 'Editar Autor'
    })
def excluir(request, id):
    autor = get_object_or_404(Autor, pk=id)
    frm = Autor_form(request.POST or None, instance= autor)
    autor.delete()
    return redirect('Autores.lista')