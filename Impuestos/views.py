from django.shortcuts import render, redirect, get_object_or_404
from .models import Impuestos
from .form import ImpuestoForm
from django.db import IntegrityError
from django.db.models import (
    ProtectedError,
)
import sweetify


def impuesto_index(request):
    impuestos_list = Impuestos.objects.all().order_by("id")

    template = "Impuestos.html"
    context = {"title": "Impuestos", "impuestos": impuestos_list}

    return render(request, template, context)


def nuevo_impuesto(request):
    if request.method == "GET":
        impuesto_form = ImpuestoForm()
        template = "nuevo_impuesto.html"
        context = {"title": "Nuevo Impuesto", "form": impuesto_form}

        return render(request, template, context)
    elif request.method == "POST":
        impuesto_form = ImpuestoForm(request.POST)
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
        impuesto_form = ImpuestoForm(request.POST, instance=impuesto_instance)
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
        impuesto_form = ImpuestoForm(instance=impuesto_instance)
        template = "nuevo_impuesto.html"
        context = {"title": "Editar Cliente", "form": impuesto_form}

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
