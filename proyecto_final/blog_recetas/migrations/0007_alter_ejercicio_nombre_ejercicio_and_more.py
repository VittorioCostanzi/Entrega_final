# Generated by Django 4.1.3 on 2022-11-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_recetas', '0006_ejercicio_grupo_muscular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='nombre_ejercicio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ejercicio',
            name='paso_a_paso',
            field=models.CharField(max_length=500),
        ),
    ]
