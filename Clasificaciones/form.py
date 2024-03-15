from django import forms
from .models import Clasificaciones

class ClasificacionesForm(forms.ModelForm):
    class Meta:
        model = Clasificaciones
        fields = ['descripcion']

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            
        }
    
        