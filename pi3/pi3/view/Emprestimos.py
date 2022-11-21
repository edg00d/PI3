from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Emprestimos_form(ModelForm):
    class Meta:
        model= Emprestimos
        fields= '__all__'
    
    def __init__(self, *args, **kwargs):
        super(Emprestimos_form, self).__init__(*args, **kwargs)
        self.fields['cpf_Usuario'].empty_label = 'Selecione um Usuário'
        self.fields['id_livro'].empty_label = 'Selecione um Livro'

def lista(request):
    return render(request, 'Emprestimos/lista.html', {
        'Emprestimos': Emprestimos.objects.all()
    })
def novo(request):
    frm = Emprestimos_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Emprestimos.lista')
    return render(request, 'Emprestimos/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Emprestimo'
    })
def editar(request, id):
    emprestimos = get_object_or_404(Emprestimos, pk=id)
    frm = Emprestimos_form(request.POST or None, instance=Emprestimos)
    if frm.is_valid():
        frm.save()
        return redirect('Emprestimos.lista')
    return render(request, 'Emprestimos/form.html',{
        'frm':frm,
        'titulo': 'Editar Emprestimos'
    })
def excluir(request, id):
    emprestimos = get_object_or_404(Emprestimos, pk=id)
    frm = Emprestimos_form(request.POST or None, instance=Emprestimos)
    emprestimos.delete()
    return redirect('Emprestimos.lista')