from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Entregable, Estudiante, Profesor, Curso, User
from .forms import ProfesorForm, EntregableForm, EstudianteForm, CursoSearchForm, CursoForm, UserCreationFormCustom, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# PROFESORES - PROFESORES - PROFESORES - PROFESORES - PROFESORES - PROFESORES - PROFESORES - PROFESORES 

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

def eliminnar_profesor(request,profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    ## contexto = {"profesores":profesor} 
    ## return render(request, "AppCoder:profesores",contexto)
    return render(request, 'profesores.html',{'profesores':profesores})

def editar_profesor(request,profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            return render(request,"inicio.html")
    else:
        miFormulario = ProfesorForm(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,
                                             'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, "editarProfesor.html",{"miFormulario":miFormulario, "profesor_nombre": profesor_nombre})

# ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - ESTUDIANTE - 
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

def eliminnar_estudiante(request,estudiante_nombre):
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    estudiante.delete()

    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html',{'estudiantes':estudiantes})

def editar_estudiante(request,estudiante_nombre):
    estudiante= Estudiante.objects.get(nombre=estudiante_nombre)
    if request.method == 'POST':
        miFormulario = EstudianteForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            
            estudiante.save()
            return render(request,"inicio.html")
    else:
        miFormulario = EstudianteForm(initial={'nombre':estudiante.nombre,'apellido':estudiante.apellido,
                                             'email': estudiante.email})
    return render(request, "editarEstudiante.html",{"miFormulario":miFormulario, "estudiante_nombre": estudiante_nombre})


# ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  ENTREGABLE -  
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

def eliminnar_entregable(request,entregable_nombre):
    entregable = Entregable.objects.get(nombre=entregable_nombre)
    entregable.delete()

    entregables = Entregable.objects.all()
    return render(request, 'entregables.html',{'entregables':entregables})

def editar_entregable(request,entregable_nombre):
    entregable= Entregable.objects.get(nombre=entregable_nombre)
    if request.method == 'POST':
        miFormulario = EntregableForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable.nombre = informacion['nombre']
            entregable.fecha_entrega = informacion['fecha_entrega']
            entregable.entregado = informacion['entregado']
            
            entregable.save()
            return render(request,"inicio.html")
    else:
        miFormulario = EntregableForm(initial={'nombre':entregable.nombre,'Fecha Entrega':entregable.fecha_entrega,
                                             'Entregado': entregable.entregado})
    return render(request, "editarentregable.html",{"miFormulario":miFormulario, "entregable_nombre": entregable_nombre})
  
# CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO - CURSO 

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
def eliminnar_curso(request,curso_nombre):
    curso = Curso.objects.get(nombre=curso_nombre)
    curso.delete()

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
def editar_curso(request,curso_nombre):
    curso= Curso.objects.get(nombre=curso_nombre)
    if request.method == 'POST':
        miFormulario = CursoForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso.nombre = informacion['nombre']
            curso.camada = informacion['camada']
                        
            curso.save()
            return render(request,"inicio.html")
    else:
        miFormulario = CursoForm(initial={'nombre':curso.nombre,'camada':curso.camada})
    return render(request, "editarcurso.html",{"miFormulario":miFormulario, "curso_nombre": curso_nombre})
class CrusoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "curso_lista.html"
class CrusodetailView(DetailView):
    model = Curso
    template_name = "AppCoder:cursos_detalle.html"
class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder:Cruso_crear.html"
    success_url  = reverse_lazy('ListaCursos')
    fields = ['nombre','camada']
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder:Cruso_editar.html"
    success_url  = reverse_lazy('ListaCursos')
    fields = ['nombre','camada']
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppCoder:Cruso_borrar.html"
    success_url  = reverse_lazy('ListaCursos')

# LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - 

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm( request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)
            return render(request, "inicio.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "login.html",{"form": form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()  
            return render(request, 'inicio.html', {"mensaje": "Usuario Creado"})
    else:
        form = UserCreationFormCustom()
    return render(request, "registro.html", {"form": form})

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():
            miFormulario.save()

            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(instance=request.user)
    return render(request,"editarPerfil.html", {"miFormulario":miFormulario})
    
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')

