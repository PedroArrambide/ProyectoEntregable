from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Entregable, Estudiante, Profesor, Curso
from .forms import ProfesorForm, EntregableForm, EstudianteForm, CursoSearchForm, CursoForm




# Create your views here.

def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def Crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:inicio')
    else:
        form = ProfesorForm()  

    return render(request, 'profesores_form.html', {'form': form})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html',{'profesores':profesores})

def Crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:inicio')
    else:
        form = EstudianteForm() 

    return render(request, 'estudiantes_form.html', {'form': form})

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html',{'estudiantes':estudiantes})



def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:inicio')
    else:
        form = EntregableForm()  

    return render(request, 'entregable_form.html', {'form': form})


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'entregables.html',{'entregables':entregables})
    

def cursoformulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:inicio')
    else:
        form = CursoForm() 
    
    return render(request, "cursoformulario.html", {'form': form})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html',{'cursos':cursos})


def buscar_cursos_por_nombre(request):
    cursos = []
    form = CursoSearchForm(request.GET)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')  # Use 'cleaned_data' instead of 'cleaned_dta'
        if nombre:
            cursos = Curso.objects.filter(nombre__icontains=nombre)  # Use 'icontains' instead of 'incontains'
    return render(request, 'buscar_cursos.html', {'form': form, 'cursos': cursos})
