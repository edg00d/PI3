from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Editora_form(ModelForm):
    class Meta:
        model= Editora
        fields= '__all__'
def lista(request):
    return render(request, 'Editoras/lista.html', {
        'Editoras': Editora.objects.all()
    })
def novo(request):
    frm = Editora_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Editoras.lista')
    return render(request, 'Editoras/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Editora'
    })
def editar(request, id):
    editora = get_object_or_404(Editora, pk=id)
    frm = Editora_form(request.POST or None, instance=Editora)
    if frm.is_valid():
        frm.save()
        return redirect('Editoras.lista')
    return render(request, 'Editoras/form.html', {
        'frm': frm,
        'titulo': 'Editar Editora'
    })
def excluir(request, id):
    editora = get_object_or_404(Editora, pk=id)
    frm = Editora_form(request.POST or None, instance=Editora)
    editora.delete()
    return redirect('Editoras.lista')