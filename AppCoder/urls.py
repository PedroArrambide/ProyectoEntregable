from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="inicio"), 
    path('cursos/', views.cursos, name="cursos"),
    path('cursoformulario', views.cursoformulario, name="cursoformulario"),
    path('buscar-por-curso/', views.buscar_cursos_por_nombre, name="buscar-por-curso"),
    path('eliminarCurso/<str:curso_nombre>/', views.eliminnar_curso, name="eliminar-curso"),
    path('editarCurso/<str:curso_nombre>/', views.editar_curso, name="editar-curso"),
    ## path('cursos/lista',views.CrusoListView.as_view(),name="ListaCursos"),
    # path('cursos/lista',views.cursos,name="ListaCursos"),
    path('cursos/nuevo',views.CursoCreateView.as_view(),name="NuevoCursos"),
    path('cursos/<pk>',views.DetailView.as_view(),name="DetalleCursos"),
    path('cursos/<pk>/editar',views.CursoUpdateView.as_view(),name="EditarCursos"),
    path('cursos/<pk>/borrar',views.CursoDeleteView.as_view(),name="BorrarCursos"),


    path('profesores', views.profesores, name="profesores"),
    path('profesor/create/', views.Crear_profesor, name="profesor-create"),
    path('eliminarProfesores/<str:profesor_nombre>/', views.eliminnar_profesor, name="eliminar-profesor"),
    path('editarProfesor/<str:profesor_nombre>/', views.editar_profesor, name="editar-profesor"),

    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('estudiante/create/', views.Crear_estudiante, name="estudiante-create"),
    path('eliminarEstudiante/<str:estudiante_nombre>/', views.eliminnar_estudiante, name="eliminar-estudiante"),
    path('editarEstudiante/<str:estudiante_nombre>/', views.editar_estudiante, name="editar-estudiante"),

    path('entregables', views.entregables, name="entregables"),
    path('entregable/create/', views.crear_entregable, name="entregable-create"),
    path('eliminarEntregable/<str:entregable_nombre>/', views.eliminnar_entregable, name="eliminar-entregable"),
    path('editarEntregable/<str:entregable_nombre>/', views.editar_entregable, name="editar-entregable"),
    
    path('login/', views.login_request, name="login"),
    path('registro/', views.registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContrasenia/',views.CambiarContrasenia.as_view() , name="CambiarContrasenia"),
    ]
