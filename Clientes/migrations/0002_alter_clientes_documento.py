# Generated by Django 4.2.10 on 2024-02-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='documento',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
