# Generated by Django 5.0.6 on 2024-07-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acostacesarapp', '0010_alter_persona_correo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='direccion',
            new_name='barrio',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='especialidad',
            new_name='disponibilidad',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='edad',
            new_name='nro',
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar_persona',
            field=models.ImageField(blank=True, null=True, upload_to='avatares_personas'),
        ),
        migrations.AddField(
            model_name='persona',
            name='calle',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='ciudad',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='estado',
            field=models.CharField(default='ACTIVO', max_length=50),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='nacionalidad',
            field=models.CharField(default='', error_messages='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='piso',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='provincia',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='servicio',
            field=models.CharField(default='OTRO', error_messages='', max_length=40),
            preserve_default=False,
        ),
    ]
