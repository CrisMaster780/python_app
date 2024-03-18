# Generated by Django 4.2.9 on 2024-03-15 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('total_presupuesto', models.FloatField()),
                ('estado_presupuesto', models.CharField(default='P', max_length=1)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePresupuestoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=250)),
                ('precio_unitario', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('total_linea', models.FloatField()),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PresupuestoCliente.presupuestocliente')),
            ],
        ),
    ]
