# Generated by Django 5.0.6 on 2024-06-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0008_alter_persona_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='especialidad',
            field=models.CharField(error_messages='', max_length=40),
        ),
    ]