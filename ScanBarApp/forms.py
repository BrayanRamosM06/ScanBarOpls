#vamos acrear el formulario usaremos la api de crispyform de django.
from django import forms
from .models import Barcode

class FormularioProducts(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = '__all__'

