# Generated by Django 4.1.3 on 2022-11-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_recetas', '0005_persona_edad_persona_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicio',
            name='grupo_muscular',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
