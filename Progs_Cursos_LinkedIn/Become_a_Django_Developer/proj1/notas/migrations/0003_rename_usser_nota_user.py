# Generated by Django 4.2.16 on 2024-11-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0002_nota_usser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='usser',
            new_name='user',
        ),
    ]
