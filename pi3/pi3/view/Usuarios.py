from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import *
from django.forms import ModelForm
class Usuario_form(ModelForm):
    class Meta:
        model= Usuario
        fields= '__all__'
def lista(request):
    return render(request, 'Usuarios/lista.html', {
        'Usuarios': Usuario.objects.all()
    })
def novo(request):
    frm = Usuario_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('Usuarios.lista')
    return render(request, 'Usuarios/form.html', {
        'frm': frm,
        'titulo': 'Cadatrar Usuario'
    })
def editar(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    frm = Usuario_form(request.POST or None, instance= usuario)
    if frm.is_valid():
        frm.save()
        return redirect('Usuarios.lista')
    return render(request, 'Usuarios/form.html',{
        'frm':frm,
        'titulo': 'Editar Usuario'
    })
def excluir(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    frm = Usuario_form(request.POST or None, instance= usuario)
    usuario.delete()
    return redirect('Usuarios.lista')