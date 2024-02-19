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


class PresupuestoClienteForm(forms.ModelForm):

    class Meta:
        model = PresupuestoCliente
        fields = ["cliente", "fecha", "total_presupuesto"]
        widgets = {
            "cliente": forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            "fecha": forms.TextInput(attrs={"class": "form-control", "type": "date"}),
            "total_presupuesto": forms.TextInput(
                attrs={"class": "form-control", "type": "number"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cliente"].empty_label = "Seleccione el Cliente"
        self.fields["cliente"].queryset = Clientes.objects.all()


class DetallePresupuestoClienteForm(forms.ModelForm):

    class Meta:
        model = DetallePresupuestoCliente
        fields = [
            "producto",
            "cantidad",
            "precio_unitario",
        ]
        widgets = {
            "producto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "text-transform: uppercase;",
                    "required": "true",
                }
            ),
            "cantidad": forms.TextInput(
                attrs={"class": "form-control ", "required": "true", "type": "number"}
            ),
            "precio_unitario": forms.TextInput(
                attrs={"class": "form-control ", "required": "true", "type": "number"}
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
