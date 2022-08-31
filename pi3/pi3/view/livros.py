from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import livro
from django.forms import ModelForm
class livro_form(ModelForm):
    class Meta:
        model= livro
        fields= '__all__'
def lista(request):
    return render(request, 'livros/lista.html', {
        'livros': livro.objects.all()
    })
def novo(request):
    frm = livro_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('livros.lista')
    return render(request, 'livros/form.html', {
        'frm': frm,
        'titulo': 'Cadatrar livro'
    })
def editar(request, id):
    livro = get_object_or_404(livro, pk=id)
    frm = livro_form(request.POST or None, instance=livro)
    if frm.is_valid():
        frm.save()
        return redirect('livros.lista')
    return render(request, 'livros/form.html',{
        'frm':frm,
        'titulo': 'Editar livro'
    })
def excluir(request, id):
    livro = get_object_or_404(livro, pk=id)
    frm = livro_form(request.POST or None, instance=livro)
    livro.delete()
    return redirect('livros.lista')