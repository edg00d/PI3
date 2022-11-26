from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Multa_form(ModelForm):
    class Meta:
        model= Multa
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super(Multa_form, self).__init__(*args, **kwargs)
        self.fields['cpf_Usuario'].empty_label = 'Selecione um Usuario'

def lista(request):
    return render(request, 'Multas/lista.html', {
        'Multas': Multa.objects.all()
    })
def novo(request):
    frm = Multa_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Multas.lista')
    return render(request, 'Multas/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Multa'
    })
def m_novo(request, dict):
    frm = Multa_form(request.POST or None, initial = dict)
    if frm.is_valid():
        frm.save()
        return redirect('Multas.lista')
    return render(request, 'Multas/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Multa'
    })
def editar(request, id):
    multa = get_object_or_404(Multa, pk=id)
    frm = Multa_form(request.POST or None, instance= multa)
    if frm.is_valid():
        frm.save()
        return redirect('Multas.lista')
    return render(request, 'Multas/form.html', {
        'frm': frm,
        'titulo': 'Editar Multa'
    })
def excluir(request, id):
    multa = get_object_or_404(Multa, pk=id)
    frm = Multa_form(request.POST or None, instance= multa)
    multa.delete()
    return redirect('Multas.lista')