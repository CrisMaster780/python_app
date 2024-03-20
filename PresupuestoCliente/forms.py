from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import PresupuestoCliente, DetallePresupuestoCliente
from Clientes.models import Clientes
from Productos.models import Productos
from django.forms import inlineformset_factory
import datetime



class CustomNumberInput(forms.widgets.NumberInput):
    template_name = "custom_number_input.html"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["attrs"][
            "step"
        ] = "1"  # Configura el paso para que no permita decimales
        return context


class TotalPresupuestoWidget(CustomNumberInput):
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super().render(name, value, attrs, **kwargs)
        return rendered + " |"  # Agrega el separador de miles al final

    def format_value(self, value):
        formatted_value = super().format_value(value)
        return formatted_value.replace(",", "|")


class PresupuestoClienteForm(forms.ModelForm):

    class Meta:
        model = PresupuestoCliente
        fields = ["cliente", "fecha", "total_presupuesto"]
        widgets = {
            "cliente": forms.Select(
                attrs={
                    "class": "form-control selectpicker",
                    "data-live-search": "true",
                    "required": "",
                }
            ),
            "fecha": forms.TextInput(attrs={"class": "form-control", "type": "date"}),
            "total_presupuesto": forms.TextInput(
                attrs={
                    "class": "form-control total_presupuesto",
                    "type": "number",
                    "readonly": "",
                    "style": "background :#1F618D;color:white",
                    "required": "",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cliente"].empty_label = "Seleccione el Cliente"
        self.fields["cliente"].queryset = Clientes.objects.all()
        if not self.initial.get("fecha"):
            # Si no hay un valor proporcionado, establecer la fecha actual
            self.initial["fecha"] = datetime.date.today()


class DetallePresupuestoClienteForm(forms.ModelForm):

    class Meta:
        model = DetallePresupuestoCliente
        fields = ["producto", "precio_unitario", "cantidad", "total_linea"]
        widgets = {
            "producto": forms.Select(
                attrs={
                    "class": "form-control selectpicker productos",
                    "data-live-search": "true",
                    "required": "",
                }
            ),
            "precio_unitario": forms.TextInput(
                attrs={
                    "class": "form-control pre_unitario",
                    "required": "true",
                    "type": "number",
                    "readonly": "true",
                }
            ),
            "cantidad": forms.TextInput(
                attrs={
                    "class": "form-control cantidad",
                    "required": "true",
                    "type": "number",
                    "min": "1",
                }
            ),
            "total_linea": forms.TextInput(
                attrs={
                    "class": "form-control total_linea",
                    "required": "true",
                    "type": "number",
                    "readonly": "",
                    "style": "background :#2E86C1;color:white",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["producto"].empty_label = "Seleccione el Producto"
        self.fields["producto"].queryset = Productos.objects.all()


class DetallePresupuestoClienteBaseFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


DetallePresupuestoClienteFormSet = inlineformset_factory(
    parent_model=PresupuestoCliente,
    model=DetallePresupuestoCliente,
    form=DetallePresupuestoClienteForm,
    formset=DetallePresupuestoClienteBaseFormSet,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
    max_num=20,
)
