from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')
