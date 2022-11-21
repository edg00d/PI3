# Generated by Django 4.1.3 on 2022-11-21 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('data_aquisicao', models.DateField()),
                ('estado', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.editora')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=13)),
                ('cep', models.CharField(max_length=9)),
                ('comp_cep', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_desbloqueio', models.DateField()),
                ('cpf_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id_livro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pi3.livro')),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('cpf_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.usuario')),
            ],
        ),
    ]
