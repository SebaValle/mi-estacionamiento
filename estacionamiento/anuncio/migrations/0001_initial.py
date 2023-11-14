# Generated by Django 4.2.7 on 2023-11-14 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dueno', models.CharField(max_length=100, verbose_name='dueño')),
                ('horario', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200, verbose_name='descripcion')),
                ('precio', models.CharField(max_length=100, verbose_name='precio')),
            ],
        ),
    ]
