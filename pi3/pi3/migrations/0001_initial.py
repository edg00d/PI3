# Generated by Django 4.1 on 2022-10-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_desbloqueio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=13)),
                ('cep', models.CharField(max_length=9)),
                ('comp_cep', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('data_aquisicao', models.DateField()),
                ('estado', models.CharField(max_length=200)),
                ('situacao_livro', models.BooleanField(null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi3.editora')),
            ],
        ),
    ]
