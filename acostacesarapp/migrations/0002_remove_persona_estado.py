# Generated by Django 5.0.6 on 2024-06-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='estado',
        ),
    ]
