from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"), 
    path('cursos/', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('entregables', views.entregables, name="entregables"),
    path('cursoformulario', views.cursoformulario, name="cursoformulario"),
    path('profesor/create/', views.Crear_profesor, name="profesor-create"),
    path('entregable/create/', views.crear_entregable, name="entregable-create"),
    path('estudiante/create/', views.Crear_estudiante, name="estudiante-create"),
    path('buscar-por-curso/', views.buscar_cursos_por_nombre, name="buscar-por-curso"),
]

