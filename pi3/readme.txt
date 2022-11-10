#python .\manage.py makemigrations crud_biblioteca
#python .\manage.py migrate
#python .\manage.py runserver
#python -m django startproject #nome_do_projeto
#cria um projeto django

Arquivo settings.py
        INSTALLED_APPS = [
            '#nome_do_projeto'
        ]
        [...]
        DATABASES = [
            'ENGINE': 'django.db.backends.mysql',
            #alteração para banco de dados mysql
            'NAME': 'pi3',
            #nome da base de dados
            'USER': 'root',
            #usuário para base de dados
            'PASSWORD': '',
            #senha para a base de dado
            'HOST':'127.0.0.1' ou 'localhost',
            'PORT': '3307'
            #porta de acesso do banco de dados
            OPTIONS': {
            'read_default_file': '/opt/lampp/etc/my.cnf'
            }
            erro com o mysql
        ]


Criação do arquivo models.py
    Onde serão representadas as entidades do banco de dados.
    As classes vão representar as tabelas e os atributos da classe vão representar as colunas.

    from django.db import models
