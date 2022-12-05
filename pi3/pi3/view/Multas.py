from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Multa_form(ModelForm):
    class Meta:
        model= Multa
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super(Multa_form, self).__init__(*args, **kwargs)
        self.fields['data_desbloqueio'].disabled = True
        self.fields['cpf_Usuario'].disabled = True
def return_date_time():
    hoje = date.today()
    return hoje + timedelta(days=10)

def lista(request):
    return render(request, 'Multas/lista.html', {
        'Multas': Multa.objects.all()
    })
def novo(request, cpf_Usuario_id):
    initial_dict = {
        "data_desbloqueio": return_date_time(),
        "cpf_Usuario": cpf_Usuario_id
    }
    frm = Multa_form(request.POST or None, initial = initial_dict)
    if frm.is_valid():
        frm.save()
        return redirect('Emprestimos.lista')
    return render(request, 'Multas/form.html', {
        'frm': frm,
        'titulo': 'Livro devolvido com atraso, multa gerada.',
        'subtitulo': 'Por favor avise o usuário que ele ficará impossibilitado de realizar emprestimos até o dia da data de desbloqueio.'
    })
def excluir(request, id):
    multa = get_object_or_404(Multa, pk=id)
    frm = Multa_form(request.POST or None, instance= multa)
    multa.delete()
    return redirect('Multas.lista')