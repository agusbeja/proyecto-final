# Generated by Django 4.1.3 on 2022-12-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0003_rename_mascotas_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=200)),
                ('ano', models.IntegerField()),
                ('kilometros', models.IntegerField()),
            ],
        ),
    ]
