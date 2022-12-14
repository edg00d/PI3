from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
from datetime import date, timedelta, timezone, datetime
from django.utils.timezone import now
class Emprestimos_form(ModelForm):
    class Meta:
        model= Emprestimos
        fields= '__all__'
    
    def __init__(self, *args, **kwargs):
        super(Emprestimos_form, self).__init__(*args, **kwargs)
        self.fields['cpf_Usuario'].empty_label = 'Selecione um Usuário'
        self.fields['id_livro'].disabled = True
        self.fields['data_emprestimo'].disabled = True

def lista(request):
    return render(request, 'Emprestimos/lista.html', {
        'Emprestimos': Emprestimos.objects.exclude(data_devolucao__isnull=False)
    })

def novo(request, id):
    initial_dict = {
        "cpf_Usuario": "",
        "id_livro": id,
        "data_emprestimo": date.today(),
    }
    frm = Emprestimos_form(request.POST or None, initial = initial_dict)
    if frm.is_valid():
        frm.save()
        livro = get_object_or_404(Livro, pk=id)
        livro.status = 0
        livro.save()
        return redirect('Livros.lista_disp')
    return render(request, 'Emprestimos/form.html', {
        'frm': frm,
        'titulo': 'Registrar Emprestimo'
    })
    
def devolver(request, id, id_livro_id, cpf_Usuario_id):
    livro = get_object_or_404(Livro, pk=id_livro_id)
    livro.status = 1
    livro.save()
    emprestimo = get_object_or_404(Emprestimos, pk=id)
    emprestimo.data_devolucao = date.today()
    emprestimo.save()
    if emprestimo.data_previ_dev < date.today():
        return redirect('Multas.novo', cpf_Usuario_id)
    else:
        return redirect('Emprestimos.lista')