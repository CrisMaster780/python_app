from django.shortcuts import render, redirect, get_object_or_404
from .models import UnidadMedida
from .form import UnidadMedidaForm
from django.db.models import Q, ProtectedError, Subquery, OuterRef, CharField, Value as V

from django.db import IntegrityError
from django.core.paginator import Paginator

from django.db.models import (
    ProtectedError,
)
import sweetify


def unidad_medida_index(request):
    template_name = 'unidad_medida.html'
    paginate_by = 10
    filter_value = request.GET.get('filter', '').strip()
    paginate_by_param = request.GET.get('paginate_by', paginate_by)

    if filter_value:
        queryset = UnidadMedida.objects.filter(
            Q(descripcion__icontains=filter_value),
            
            
        )
    else:
        queryset = UnidadMedida.objects.filter()

    paginator = Paginator(queryset, per_page=paginate_by_param)
    page = request.GET.get('page')
    blocks = paginator.get_page(page)

    context = {
        'page_obj': blocks,
        'title': 'Unidad de Medida',
        'filter': filter_value,
    }
        
    return render(request, template_name, context)



def nueva_unidad_medida(request):
    if request.method == "GET":
        unidad_medida_form = UnidadMedidaForm()
        template = "nueva_unidad_medida.html"
        context = {"title": "Nueva Unidad de Medida", "form": unidad_medida_form}

        return render(request, template, context)
    elif request.method == "POST":
        unidad_medida_form = UnidadMedidaForm(request.POST)
        if unidad_medida_form.is_valid():
            try:
                unidad_medida_form.save()
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
        return redirect("unidades")


def modificar_unidad_medida(request, id):
    unidad_medida_instance = get_object_or_404(UnidadMedida, id=id)
    if request.method == "POST":
        unidad_medida_form = UnidadMedidaForm(request.POST, instance=unidad_medida_instance)
        try:
            if unidad_medida_form.is_valid():
                unidad_medida_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("unidades")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        unidad_medida_form = UnidadMedidaForm(instance=unidad_medida_instance)
        template = "nueva_unidad_medida.html"
        context = {"title": "Editar Unidad de Medida", "form": unidad_medida_form}

        return render(request, template, context)



def eliminar_unidad_medida(request, id):
    objeto = get_object_or_404(UnidadMedida, id=id)

    try:
        objeto.delete()
        sweetify.toast(request, "El proceso de borrado se ha realizado con éxito.")
    except ProtectedError as e:
        related_models = [
            obj.related_model._meta.verbose_name_plural for obj in e.protected_objects
        ]
        message = 'El registro no puede ser eliminado, porque está siendo utilizado en otra Entidad'
        sweetify.toast(request, message, icon="error", timer=5000)

    return redirect("unidades")