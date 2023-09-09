from django import forms
from .models import  Entregable, Profesor, Estudiante, Curso, User
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm

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
    camada = forms.IntegerField(required=False)

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre")
    last_name = forms.CharField(label= "Apellido")
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):

    password=None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ['email','last_name','first_name']