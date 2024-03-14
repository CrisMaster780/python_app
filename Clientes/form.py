from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre','apellido','direccion','telefono','correo','documento','observacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'observacion':forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            
        }
    
        