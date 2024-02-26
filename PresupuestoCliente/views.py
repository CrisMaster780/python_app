from django.shortcuts import render, redirect , get_object_or_404
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DetallePresupuestoCliente
from .forms import PresupuestoClienteForm, DetallePresupuestoClienteForm, DetallePresupuestoClienteFormSet
from .models import PresupuestoCliente
import sweetify


def index_presupuesto(request):
    presupuesto_list = PresupuestoCliente.objects.all().order_by("id")
    paginator = Paginator(presupuesto_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    final_page_number = paginator.num_pages - 1
    template = "index_presupuesto.html"
    context = {"titulo": "Presupuestos", "presupuesto": page_obj, "final_page_number": final_page_number}

    return render(request, template, context)

def crearPresupuesto(request):
    if request.method == 'POST':
        presupuesto_cliente_form = PresupuestoClienteForm(request.POST)
        detalle_presupuesto_cliente_formset = DetallePresupuestoClienteFormSet(request.POST, prefix='details')

        try:
            if presupuesto_cliente_form.is_valid() and detalle_presupuesto_cliente_formset.is_valid():
                with transaction.atomic():
                    presupuesto_cliente_instance = presupuesto_cliente_form.save()
                    detalle_presupuesto_cliente_formset.instance = presupuesto_cliente_instance
                    detalle_presupuesto_cliente_formset.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect('presupuesto')
        except IntegrityError as e:
            sweetify.toast(
                    request,
                    "Oops, Ocurrió un error al momento del guardado",
                    icon="error",
                    timer=3000,
                )
    else:
        presupuesto_cliente_form = PresupuestoClienteForm()
        detalle_presupuesto_cliente_formset = DetallePresupuestoClienteFormSet(prefix='details')

    context = {
        'presupuesto': presupuesto_cliente_form,
        'details': detalle_presupuesto_cliente_formset,
        'titulo': 'Presupuesto Cliente',
    }
    return render(request, 'crearPresupuesto.html', context)

def detallePresupuesto(request, id):
    detalles = DetallePresupuestoCliente.objects.filter(presupuesto_id=id)
    presupuesto = get_object_or_404(PresupuestoCliente, id=id)
    context = {
        'detalles': detalles,
        'presupuesto': presupuesto, 
        'titulo': 'Detalle Presupuesto Cliente',
    }
    return render(request, 'detallePresupuesto.html', context)
    