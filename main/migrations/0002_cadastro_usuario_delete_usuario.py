# Generated by Django 4.0.6 on 2022-08-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
