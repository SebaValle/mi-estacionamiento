from django import forms
from .models import publicacion
from .models import Usuario


class anuncioForm(forms.ModelForm):
    class Meta:
        model = publicacion
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'password']