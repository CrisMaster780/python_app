from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import PresupuestoCliente, DetallePresupuestoCliente
from Clientes.models import Clientes
from django.forms import inlineformset_factory
import datetime


class PresupuestoClienteForm(forms.ModelForm):

    class Meta:
        model = PresupuestoCliente
        fields = ["cliente", "fecha", "total_presupuesto"]
        widgets = {
            "cliente": forms.Select(
                attrs={"class": "form-control selectpicker", "data-live-search": "true", "required": ""}
            ),
            "fecha": forms.TextInput(attrs={"class": "form-control", "type": "date"}),
            "total_presupuesto": forms.TextInput(
                attrs={"class": "form-control total_presupuesto", "type": "number", "readonly": "","style":"background :#1F618D;color:white", "required": ""}
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
        fields = ["producto", "cantidad", "precio_unitario", "total_linea"]
        widgets = {
            "producto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": "true",
                    'onkeyup': 'this.value = this.value.toUpperCase();'
                }
            ),
            "cantidad": forms.TextInput(
                attrs={"class": "form-control cantidad", "required": "true", "type": "number","min":"1"}
            ),
            "precio_unitario": forms.TextInput(
                attrs={"class": "form-control pre_unitario", "required": "true", "type": "number"}
            ),
            "total_linea": forms.TextInput(
                attrs={"class": "form-control total_linea", "required": "true", "type": "number", "readonly":"", "style":"background :#2E86C1;color:white"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
