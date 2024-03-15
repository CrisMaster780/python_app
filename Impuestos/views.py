from django.shortcuts import render, redirect, get_object_or_404
from .models import Impuestos
from .form import ImpuestosForm
from django.db.models import Q, ProtectedError, Subquery, OuterRef, CharField, Value as V

from django.db import IntegrityError
from django.core.paginator import Paginator

from django.db.models import (
    ProtectedError,
)
import sweetify


def impuesto_index(request):
    template_name = 'impuestos_index.html'
    paginate_by = 10
    filter_value = request.GET.get('filter', '').strip()
    paginate_by_param = request.GET.get('paginate_by', paginate_by)

    if filter_value:
        queryset = Impuestos.objects.filter(
            Q(descripcion__icontains=filter_value),
            
            
        )
    else:
        queryset = Impuestos.objects.filter()

    paginator = Paginator(queryset, per_page=paginate_by_param)
    page = request.GET.get('page')
    blocks = paginator.get_page(page)

    context = {
        'page_obj': blocks,
        'title': 'Impuestos',
        'filter': filter_value,
    }
        
    return render(request, template_name, context)



def nuevo_impuesto(request):
    if request.method == "GET":
        impuesto_form = ImpuestosForm()
        template = "nuevo_impuesto.html"
        context = {"title": "Nuevo Impuesto", "form": impuesto_form}

        return render(request, template, context)
    elif request.method == "POST":
        impuesto_form = ImpuestosForm(request.POST)
        if impuesto_form.is_valid():
            try:
                impuesto_form.save()
                sweetify.toast(request, "Guardado Exitoso")
            except:
                sweetify.toast(
                    request,
                    "Oops, Ocurrió un error al momento del guardado",
                    icon="error",
                    timer=3000,
                )
        else:
            sweetify.toast(
                request,
                "Oops, Ocurrió un error. Verifica los campos del formulario.",
                icon="error",
                timer=3000,
            )
        return redirect("impuestos")


def modificar_impuesto(request, id):
    impuesto_instance = get_object_or_404(Impuestos, id=id)
    if request.method == "POST":
        impuesto_form = ImpuestosForm(request.POST, instance=impuesto_instance)
        try:
            if impuesto_form.is_valid():
                impuesto_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("impuestos")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        impuesto_form = ImpuestosForm(instance=impuesto_instance)
        template = "nuevo_impuesto.html"
        context = {"title": "Editar Impuesto", "form": impuesto_form}

        return render(request, template, context)



def eliminar_impuesto(request, id):
    objeto = get_object_or_404(Impuestos, id=id)

    try:
        objeto.delete()
        sweetify.toast(request, "El proceso de borrado se ha realizado con éxito.")
    except ProtectedError as e:
        related_models = [
            obj.related_model._meta.verbose_name_plural for obj in e.protected_objects
        ]
        message = 'El registro no puede ser eliminado, porque está siendo utilizado en otra Entidad'
        sweetify.toast(request, message, icon="error", timer=5000)

    return redirect("impuestos")