from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre','descripcion', 'precio', 'stock', 'estado', 'registered_by']  # Incluye registered_by si deseas que sea visible

