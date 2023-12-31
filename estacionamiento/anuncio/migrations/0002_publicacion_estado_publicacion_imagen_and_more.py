# Generated by Django 4.2.7 on 2023-11-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='estado',
            field=models.CharField(default='libre', max_length=100, verbose_name='estado'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='descripcion',
            field=models.TextField(max_length=300, verbose_name='descripcion'),
        ),
    ]
