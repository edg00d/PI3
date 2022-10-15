from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import editora
from django.forms import ModelForm
class editora_form(ModelForm):
    class Meta:
        model= editora
        fields= '__all__'
def lista(request):
    return render(request, 'editoras/lista.html', {
        'editoras': editora.objects.all()
    })
def novo(request):
    frm = editora_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('editoras.lista')
    return render(request, 'editoras/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar editora'
    })
def editar(request, id):
    Editora = get_object_or_404(editora, pk=id)
    frm = editora_form(request.POST or None, instance=editora)
    if frm.is_valid():
        frm.save()
        return redirect('editoras.lista')
    return render(request, 'editoras/form.html', {
        'frm': frm,
        'titulo': 'Editar editora'
    })
def excluir(request, id):
    Editora = get_object_or_404(editora, pk=id)
    frm = editora_form(request.POST or None, instance=editora)
    Editora.delete()
    return redirect('editoras.lista')