# Generated by Django 5.0.6 on 2024-06-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0009_alter_persona_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=40),
        ),
    ]
