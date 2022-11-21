"""
pi3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pi3.view import pages, Autores, Editoras, Livros, Usuarios, Multas, Emprestimos

urlpatterns = [
    path('', pages.home, name='home'),

    path('Autores', Autores.lista, name='Autores.lista'),
    path('Autores/novo', Autores.novo, name='Autores.novo'),
    path('Autores/editar/<id>', Autores.editar, name='Autores.editar'),
    path('Autores/excluir/<id>', Autores.excluir, name='Autores.excluir'),
    
    path('Editoras', Editoras.lista, name='Editoras.lista'),
    path('Editoras/novo', Editoras.novo, name='Editoras.novo'),
    path('Editoras/editar/<id>', Editoras.editar, name='Editoras.editar'),
    path('Editoras/excluir/<id>', Editoras.excluir, name='Editoras.excluir'),

    path('Livros', Livros.lista, name='Livros.lista'),
    path('Livros/novo', Livros.novo, name='Livros.novo'),
    path('Livros/editar/<id>', Livros.editar, name='Livros.editar'),
    path('Livros/excluir/<id>', Livros.excluir, name='Livros.excluir'),

    path('Usuarios', Usuarios.lista, name='Usuarios.lista'),
    path('Usuarios/novo', Usuarios.novo, name='Usuarios.novo'),
    path('Usuarios/editar/<id>', Usuarios.editar, name='Usuarios.editar'),
    path('Usuarios/excluir/<id>', Usuarios.excluir, name='Usuarios.excluir'),

    path('Multas', Multas.lista, name='Multas.lista'),
    path('Multas/novo', Multas.novo, name='Multas.novo'),
    path('Multas/editar/<id>', Multas.editar, name='Multas.editar'),
    path('Multas/excluir/<id>', Multas.excluir, name='Multas.excluir'),

    path('Emprestimos', Emprestimos.lista, name='Emprestimos.lista'),
    path('Emprestimos/novo', Emprestimos.novo, name='Emprestimos.novo'),
    path('Emprestimos/editar/<id>', Emprestimos.editar, name='Emprestimos.editar'),
    path('Emprestimos/excluir/<id>', Emprestimos.excluir, name='Emprestimos.excluir'),
]