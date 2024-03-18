# Generated by Django 4.2.9 on 2024-03-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('documento', models.CharField(max_length=250)),
                ('ruc', models.CharField(blank=True, max_length=250, null=True)),
                ('observacion', models.CharField(max_length=250)),
                ('estado', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
    ]
