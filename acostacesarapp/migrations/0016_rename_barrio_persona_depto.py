# Generated by Django 5.0.6 on 2024-07-03 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0015_remove_persona_fecha_nac'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='barrio',
            new_name='depto',
        ),
    ]
