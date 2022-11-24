from django.shortcuts import render
def home(request):
    return render(request, 'pages/home.html', {

    })
def home_acervo(request):
    return render(request, 'pages/home_acervo.html', {

    })
def home_usuario(request):
    return render(request, 'pages/home_usuario.html', {

    })
def home_empr(request):
    return render(request, 'pages/home_empr.html', {

    })