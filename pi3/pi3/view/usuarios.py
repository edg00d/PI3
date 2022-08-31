from django.shortcuts import render, redirect, get_object_or_404
from pi3.models import usuario
from django.forms import ModelForm
class usuario_form(ModelForm):
    class Meta:
        model= usuario
        fields= '__all__'
def lista(request):
    return render(request, 'usuarios/lista.html', {
        'usuarios': usuario.objects.all()
    })
def novo(request):
    frm = usuario_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('usuarios.lista')
    return render(request, 'usuarios/form.html', {
        'frm': frm,
        'titulo': 'Cadatrar usuario'
    })
def editar(request, id):
    usuario = get_object_or_404(usuario, pk=id)
    frm = usuario_form(request.POST or None, instance=usuario)
    if frm.is_valid():
        frm.save()
        return redirect('usuarios.lista')
    return render(request, 'usuarios/form.html',{
        'frm':frm,
        'titulo': 'Editar usuario'
    })
def excluir(request, id):
    usuario = get_object_or_404(usuario, pk=id)
    frm = usuario_form(request.POST or None, instance=usuario)
    usuario.delete()
    return redirect('usuarios.lista')