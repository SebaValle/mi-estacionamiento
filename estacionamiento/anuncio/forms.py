from django import forms
from .models import publicacion



class anuncioForm(forms.ModelForm):
    class Meta:
        model = publicacion
        fields = '__all__'

