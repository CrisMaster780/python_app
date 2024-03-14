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
            Q(nombre__icontains=filter_value),
            Q(apellido__icontains=filter_value),
            
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

""" 


def nuevo_producto(request):
    if request.method == "GET":
        producto_form = ProductosForm()
        template = "nuevo_producto.html"
        context = {"title": "Nuevo Producto", "form": producto_form}

        return render(request, template, context)
    elif request.method == "POST":
        producto_form = ProductosForm(request.POST)
        if producto_form.is_valid():
            try:
                producto_form.save()
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
        return redirect("productos")





def modificar_producto(request, id):
    producto_instance = get_object_or_404(Productos, id=id)
    if request.method == "POST":
        producto_form = ProductosForm(request.POST, instance=producto_instance)
        try:
            if producto_form.is_valid():
                producto_form.save()
                sweetify.toast(request, "Guardado Exitoso")
                return redirect("productos")
        except IntegrityError as e:
            sweetify.toast(
                request,
                "Algunos de los datos deben ser únicos y ya existen en la base de datos.",
                icon="error",
                timer=3000,
            )
    else:
        producto_form = ProductosForm(instance=producto_instance)
        template = "nuevo_producto.html"
        context = {"title": "Editar Producto", "form": producto_form}

        return render(request, template, context)

def eliminar_producto(request, id):
    objeto = get_object_or_404(Productos, id=id)

    try:
        objeto.delete()
        sweetify.toast(request, "El proceso de borrado se ha realizado con éxito.")
    except ProtectedError as e:
        related_models = [
            obj.related_model._meta.verbose_name_plural for obj in e.protected_objects
        ]
        message = 'El registro no puede ser eliminado, porque está siendo utilizado en otra Entidad'
        sweetify.toast(request, message, icon="error", timer=5000)

    return redirect("productos")

 """