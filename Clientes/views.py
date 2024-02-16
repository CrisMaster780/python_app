from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from .form import ClientesForm
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.db.models import (
    ProtectedError,
)
import sweetify


def clientes_index(request):
    clientes_list = Clientes.objects.all().order_by("nombre")
    paginator = Paginator(clientes_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Calcula el número de la última página
    final_page_number = paginator.num_pages - 1

    template = "clientes_index.html"
    context = {"titulo": "Clientes", "clientes": page_obj, "final_page_number": final_page_number}

    return render(request, template, context)


def nuevo_cliente(request):
    if request.method == "GET":
        cliente_form = ClientesForm()
        template = "nuevo_cliente.html"
        context = {"titulo": "Nuevo Cliente", "form": cliente_form}

        return render(request, template, context)
    elif request.method == "POST":
        cliente_form = ClientesForm(request.POST)
        if cliente_form.is_valid():
            try:
                cliente_form.save()
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
        return redirect("clientes")


def modificar_cliente(request, id):
    cliente_instance = get_object_or_404(Clientes, id=id)
    if request.method == "POST":
        cliente_form = ClientesForm(request.POST, instance=cliente_instance)
        try:
            if cliente_form.is_valid():
                cliente_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("clientes")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        cliente_form = ClientesForm(instance=cliente_instance)
        template = "nuevo_cliente.html"
        context = {"titulo": "Editar Cliente", "form": cliente_form}

        return render(request, template, context)


def eliminar_cliente(request, id):
    objeto = get_object_or_404(Clientes, id=id)

    try:
        objeto.delete()
        sweetify.toast(request, "El proceso de borrado se ha realizado con éxito.")
    except ProtectedError as e:
        related_models = [
            obj.related_model._meta.verbose_name_plural for obj in e.protected_objects
        ]
        message = f'El registro no puede ser eliminado, porque está siendo utilizado en la entidad: <li>{"<li>".join(related_models)}'
        sweetify.toast(request, message, icon="error", timer=3000)

    return redirect("clientes")
