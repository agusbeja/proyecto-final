from django import forms
from ejemplo.models import Familiar, Mascota, Auto


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class BuscarCar(forms.Form):
    marca = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']


class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'tipo', 'raza', 'edad']


class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['marca', 'modelo', 'ano', 'kilometros']





