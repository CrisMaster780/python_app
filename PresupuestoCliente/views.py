from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from django.contrib import messages
from .forms import PresupuestoClienteForm, DetallePresupuestoClienteForm, DetallePresupuestoClienteFormSet
from .models import PresupuestoCliente

def index_presupuesto(request):
    if request.method == 'POST':
        presupuesto_cliente_form = PresupuestoClienteForm(request.POST)
        detalle_presupuesto_cliente_formset = DetallePresupuestoClienteFormSet(request.POST, prefix='details')

        try:
            if presupuesto_cliente_form.is_valid() and detalle_presupuesto_cliente_formset.is_valid():
                with transaction.atomic():
                    presupuesto_cliente_instance = presupuesto_cliente_form.save()
                    detalle_presupuesto_cliente_formset.instance = presupuesto_cliente_instance
                    detalle_presupuesto_cliente_formset.save()
                messages.success(request, 'Guardado Exitoso')
                return redirect('presupuesto')
        except IntegrityError as e:
            messages.error(request, 'Algunos de los datos deben ser únicos y ya existen en la base de datos.')
    else:
        presupuesto_cliente_form = PresupuestoClienteForm()
        detalle_presupuesto_cliente_formset = DetallePresupuestoClienteFormSet(prefix='details')

    context = {
        'presupuesto': presupuesto_cliente_form,
        'details': detalle_presupuesto_cliente_formset,
        'titulo': 'Presupuesto Cliente',
    }
    return render(request, 'index.html', context)

