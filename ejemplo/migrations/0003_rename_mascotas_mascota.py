# Generated by Django 4.1.3 on 2022-12-11 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_mascotas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mascotas',
            new_name='Mascota',
        ),
    ]
