# Generated by Django 4.0.6 on 2022-08-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='produto/'),
        ),
    ]
