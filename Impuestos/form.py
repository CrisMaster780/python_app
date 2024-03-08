from django import forms
from .models import Impuestos

class ImpuestoForm(forms.ModelForm):
    class Meta:
        model = Impuestos
        fields = ['descripcion','porcentaje']

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'porcentaje': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
           
        }