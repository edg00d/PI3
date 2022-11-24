from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *

def lista(request):
    return render(request, 'Hist_Empr/lista.html', {
        'Hist_Empr': Emprestimos.objects.exclude(data_devolucao__isnull=True)
    })