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
from pi3.view import pages, autores, editoras, livros, usuarios

urlpatterns = [
    path('', pages.home, name='home'),

    path('autores', autores.lista, name='autores.lista'),
    path('autores/novo', autores.novo, name='autores.novo'),
    path('autores/editar/<id>', autores.editar, name='autores.editar'),
    path('autores/excluir/<id>', autores.excluir, name='autores.excluir'),
    
    path('editoras', editoras.lista, name='editoras.lista'),
    path('editoras/novo', editoras.novo, name='editoras.novo'),
    path('editoras/editar/<id>', editoras.editar, name='editoras.editar'),
    path('editoras/excluir/<id>', editoras.excluir, name='editoras.excluir'),

    path('livros', livros.lista, name='livros.lista'),
    path('livros/novo', livros.novo, name='livros.novo'),
    path('livros/editar/<id>', livros.editar, name='livros.editar'),
    path('livros/excluir/<id>', livros.excluir, name='livros.excluir'),

    path('usuarios', usuarios.lista, name='usuarios.lista'),
    path('usuarios/novo', usuarios.novo, name='usuarios.novo'),
    path('usuarios/editar/<id>', usuarios.editar, name='usuarios.editar'),
    path('usuarios/excluir/<id>', usuarios.excluir, name='usuarios.excluir'),
]