from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from .form import ClientesForm
from django.db.models import Q, ProtectedError, Subquery, OuterRef, CharField, Value as V

from django.db import IntegrityError
from django.core.paginator import Paginator

from django.db.models import (
    ProtectedError,
)
import sweetify


def cliente_index(request):
    template_name = 'cliente_index.html'
    paginate_by = 10
    filter_value = request.GET.get('filter', '').strip()
    paginate_by_param = request.GET.get('paginate_by', paginate_by)

    if filter_value:
        queryset = Clientes.objects.filter(
            Q(documento__icontains=filter_value),
            
            
        )
    else:
        queryset = Clientes.objects.filter()

    paginator = Paginator(queryset, per_page=paginate_by_param)
    page = request.GET.get('page')
    blocks = paginator.get_page(page)

    context = {
        'page_obj': blocks,
        'title': 'Clientes',
        'filter': filter_value,
    }
        
    return render(request, template_name, context)




def nuevo_cliente(request):
    if request.method == "GET":
        cliente_form = ClientesForm()
        template = "nuevo_cliente.html"
        context = {"title": "Nuevo Cliente", "form": cliente_form}

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
        context = {"title": "Editar Cliente", "form": cliente_form}

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
        message = 'El registro no puede ser eliminado, porque está siendo utilizado en otra Entidad'
        sweetify.toast(request, message, icon="error", timer=5000)

    return redirect("clientes")

