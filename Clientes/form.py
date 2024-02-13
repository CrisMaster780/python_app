from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'documento', 'direccion', 'correo', 'telefono', 'estado', 'observacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();', 'required': ''}),

            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
