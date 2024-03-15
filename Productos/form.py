from django import forms
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['descripcion','codigo_barra','codigo_remitido','precio_costo','precio_venta','precio_mayorista','existencia','clasificacion', 'impuesto']

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'codigo_barra': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'codigo_remitido': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();'}),
            'precio_costo': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();', 'type': 'number'}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();', 'type': 'number'}),
            'precio_mayorista': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();', 'type': 'number'}),
            'existencia':forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'this.value = this.value.toUpperCase();' , 'type': 'number'}),
            'impuesto': forms.Select(attrs={'class': 'form-select selectpicker w-100', 'data-live-search': 'true'}),
            'clasificacion': forms.Select(attrs={'class': 'form-select selectpicker w-100', 'data-live-search': 'true'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-select selectpicker w-100', 'data-live-search': 'true'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clasificacion'].empty_label = "Seleccione la Clasificacion"
        self.fields['impuesto'].empty_label = "Seleccione el Impuesto"
        """
         self.fields['unidad_medida'].empty_label = "Seleccione la Unidad de Medida" 
        ,'impuesto','clasificacion','unidad_medida'
        
        """
        