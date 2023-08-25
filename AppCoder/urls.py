from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('entregables', views.entregables, name="entregables"),
    path('cursoformulario', views.cursoformulario, name="cursoformulario"),
    path('entregable_form', views.entregable_form, name="entregable_form"),
]

