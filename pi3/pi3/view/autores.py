from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import autor
from django.forms import ModelForm
class autor_form(ModelForm):
    class Meta:
        model= autor
        fields= '__all__'
def lista(request):
    return render(request, 'autores/lista.html', {
        'autores': autor.objects.all()
    })
def novo(request):
    frm = autor_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('autores.lista')
    return render(request, 'autores/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar autor'
    })
def editar(request, id):
    Autor = get_object_or_404(autor, pk=id)
    frm = autor_form(request.POST or None, instance=autor)
    if frm.is_valid():
        frm.save()
        return redirect('autores.lista')
    return render(request, 'autores/form.html', {
        'frm': frm,
        'titulo': 'Editar autor'
    })
def excluir(request, id):
    Autor = get_object_or_404(autor, pk=id)
    frm = autor_form(request.POST or None, instance=autor)
    Autor.delete()
    return redirect('autores.lista')