# Generated by Django 4.1.3 on 2022-11-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_recetas', '0008_rename_ciudad_persona_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
