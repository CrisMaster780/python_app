from django.shortcuts import render, redirect, get_object_or_404
from .models import Clasificaciones
from .form import ClasificacionForm
from django.db import IntegrityError
from django.db.models import (
    ProtectedError,
)
import sweetify


def clasificacion_index(request):
    clasificaciones_list = Clasificaciones.objects.all().order_by("id")

    template = "Clasificaciones.html"
    context = {"title": "Clasificaciones", "clasificaciones": clasificaciones_list}

    return render(request, template, context)


def nueva_clasificacion(request):
    if request.method == "GET":
        clasificacion_form = ClasificacionForm()
        template = "nueva_clasificacion.html"
        context = {"title": "Nuevo Impuesto", "form": clasificacion_form}

        return render(request, template, context)
    elif request.method == "POST":
        clasificacion_form = ClasificacionForm(request.POST)
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
        clasificacion_form = ClasificacionForm(request.POST, instance=clasificacion_instance)
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
        clasificacion_form = ClasificacionForm(instance=clasificacion_instance)
        template = "nueva_clasificacion.html"
        context = {"title": "Editar Cliente", "form": clasificacion_form}

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
