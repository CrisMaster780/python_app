from django.shortcuts import render, redirect, get_object_or_404
from .models import Clasificaciones
from .form import ClasificacionesForm
from django.db.models import Q, ProtectedError, Subquery, OuterRef, CharField, Value as V

from django.db import IntegrityError
from django.core.paginator import Paginator

from django.db.models import (
    ProtectedError,
)
import sweetify


def clasificaciones_index(request):
    template_name = 'clasificaciones_index.html'
    paginate_by = 10
    filter_value = request.GET.get('filter', '').strip()
    paginate_by_param = request.GET.get('paginate_by', paginate_by)

    if filter_value:
        queryset = Clasificaciones.objects.filter(
            Q(descripcion__icontains=filter_value),
            
            
        )
    else:
        queryset = Clasificaciones.objects.filter()

    paginator = Paginator(queryset, per_page=paginate_by_param)
    page = request.GET.get('page')
    blocks = paginator.get_page(page)

    context = {
        'page_obj': blocks,
        'title': 'Clasificaciones',
        'filter': filter_value,
    }
        
    return render(request, template_name, context)



def nueva_clasificacion(request):
    if request.method == "GET":
        clasificacion_form = ClasificacionesForm()
        template = "nueva_clasificacion.html"
        context = {"title": "Nueva Clasificación", "form": clasificacion_form}

        return render(request, template, context)
    elif request.method == "POST":
        clasificacion_form = ClasificacionesForm(request.POST)
        if clasificacion_form.is_valid():
            try:
                clasificacion_form.save()
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
        return redirect("clasificaciones")


def modificar_clasificacion(request, id):
    clasificacion_instance = get_object_or_404(Clasificaciones, id=id)
    if request.method == "POST":
        clasificacion_form = ClasificacionesForm(request.POST, instance=clasificacion_instance)
        try:
            if clasificacion_form.is_valid():
                clasificacion_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("clasificaciones")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        clasificacion_form = ClasificacionesForm(instance=clasificacion_instance)
        template = "nueva_clasificacion.html"
        context = {"title": "Editar Clasificación", "form": clasificacion_form}

        return render(request, template, context)



def eliminar_clasificacion(request, id):
    objeto = get_object_or_404(Clasificaciones, id=id)

    try:
        objeto.delete()
        sweetify.toast(request, "El proceso de borrado se ha realizado con éxito.")
    except ProtectedError as e:
        related_models = [
            obj.related_model._meta.verbose_name_plural for obj in e.protected_objects
        ]
        message = 'El registro no puede ser eliminado, porque está siendo utilizado en otra Entidad'
        sweetify.toast(request, message, icon="error", timer=5000)

    return redirect("clasificaciones")