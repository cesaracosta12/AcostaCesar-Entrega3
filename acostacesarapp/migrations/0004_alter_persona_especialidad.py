# Generated by Django 5.0.6 on 2024-06-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0003_alter_persona_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='especialidad',
            field=models.CharField(choices=[('GASISTA', 'Gasista'), ('ELECTRICISTA', 'Electricista')], max_length=40),
        ),
    ]
