# Generated by Django 4.1.2 on 2022-10-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteon4', '0005_remove_usuarios_anotacoes_anotacoes_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anotacoes',
            name='usuarios',
        ),
    ]