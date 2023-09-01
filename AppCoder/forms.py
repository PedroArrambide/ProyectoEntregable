from django import forms
from .models import  Entregable, Profesor, Estudiante, Curso

class EntregableForm(forms.ModelForm):
    class Meta:
        model= Entregable
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields = '__all__'

class CursoSearchForm(forms.Form):
    nombre = forms.CharField(required=False)