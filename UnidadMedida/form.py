from django import forms
from .models import UnidadMedida

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'resumido']

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'resumido': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            
        }
    
        