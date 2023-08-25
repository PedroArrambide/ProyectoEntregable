from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso, Entregable, Estudiante, Profesor




# Create your views here.

def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores__(request):
    return render(request, 'profesores.html')

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html',{'profesores':profesores})

def estudiantes__(request):
    return render(request, 'estudiantes.html')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html',{'estudiantes':estudiantes})



def entregable_form(request):
    if request.method == 'POST':
        form = entregable_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Appcoder:inicio')
    else:
        form = entregable_form()  
    return render(request, 'entregables.html', {'form': form})


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'entregables.html',{'entregables':entregables})
    

def cursoformulario(request):
    if request.method == 'POST':
        curso = curso(request.post["curso"],request.post["camada"])
        curso.save()
        return render(request, 'AppCoder:inicio.html')
    
    return render(request, "cursoformulario.html")

