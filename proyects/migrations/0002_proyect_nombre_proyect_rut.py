# Generated by Django 4.2.7 on 2024-12-05 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=200),
        ),
        migrations.AddField(
            model_name='proyect',
            name='rut',
            field=models.CharField(default='Sin RUT', max_length=200),
        ),
    ]
