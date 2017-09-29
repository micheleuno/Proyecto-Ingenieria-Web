from django.conf.urls import url

from . import views

app_name = 'Nave'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^estudiante/$', views.ViewEstudiante.as_view(), name='estudiante'),
    url(r'^profesor/$', views.Profesor.as_view(), name='profesor'),
    url(r'^administrador/$', views.Administrador.as_view(), name='administrador'),
    url('editar_estudiante/', views.editar_estudiante, name='editar_estudiante'),    
	url('guardar_estudiante/', views.guardar_estudiante, name='guardar_estudiante'),
	url('filtrar_ramos_estudiante/', views.filtrar_ramos_estudiante, name='filtrar_ramos_estudiante'),
	url('filtrar_ramos_profesor/', views.filtrar_ramos_profesor, name='filtrar_ramos_profesor'),
	url('filtrar_alumnos_profesor/', views.filtrar_alumnos_profesor, name='filtrar_alumnos_profesor'),
]