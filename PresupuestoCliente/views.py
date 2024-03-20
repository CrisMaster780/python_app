from django.shortcuts import render, redirect , get_object_or_404
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DetallePresupuestoCliente
from django.db.models import Q, ProtectedError, Subquery, OuterRef, CharField, Value as V

from .forms import PresupuestoClienteForm, DetallePresupuestoClienteForm, DetallePresupuestoClienteFormSet
from .models import PresupuestoCliente
import sweetify
from django.http import JsonResponse
from Productos.models import Productos


def index_presupuesto(request):
    template_name = 'index_presupuesto.html'
    paginate_by = 10
    filter_value = request.GET.get('filter', '').strip()
    paginate_by_param = request.GET.get('paginate_by', paginate_by)

    if filter_value:
        queryset = PresupuestoCliente.objects.filter(
            Q(cliente__nombre__icontains=filter_value),
            
            
        )
    else:
        queryset = PresupuestoCliente.objects.filter()

    paginator = Paginator(queryset, per_page=paginate_by_param)
    page = request.GET.get('page')
    blocks = paginator.get_page(page)

    context = {
        'page_obj': blocks,
        'title': 'Presupuesto',
        'filter': filter_value,
    }
        
    return render(request, template_name, context)

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

def obtenerPrecioUnitario(request, id_producto):
    try:
        producto = Productos.objects.get(id=id_producto)
        precio_unitario = producto.precio_venta
        iva = producto.impuesto.porcentaje
        data = {'precio_unitario': precio_unitario, "iva":iva}
        return JsonResponse(data)
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)