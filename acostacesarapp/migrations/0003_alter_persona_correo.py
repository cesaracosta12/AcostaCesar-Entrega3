# Generated by Django 5.0.6 on 2024-06-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0002_remove_persona_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=20),
        ),
    ]
