from django.shortcuts import render, redirect, get_object_or_404
from .models import UnidadMedida
from .form import UnidadMedidaForm
from django.db import IntegrityError
from django.db.models import (
    ProtectedError,
)
import sweetify


def unidad_medida_index(request):
    unidad_medida_list = UnidadMedida.objects.all().order_by("id")

    template = "UnidadMedida.html"
    context = {"title": "UnidadMedida", "unidad_medida": unidad_medida_list}

    return render(request, template, context)


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
        return redirect("unidad_medida")


def modificar_unidad_medida(request, id):
    unidad_medida_instance = get_object_or_404(UnidadMedida, id=id)
    if request.method == "POST":
        unidad_medida_form = UnidadMedidaForm(request.POST, instance=unidad_medida_instance)
        try:
            if unidad_medida_form.is_valid():
                unidad_medida_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("unidad_medida")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        unidad_medida_form = UnidadMedidaForm(instance=unidad_medida_instance)
        template = "nueva_clasificacion.html"
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

    return redirect("unidad_medida")
