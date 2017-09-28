from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^estudiante/$', views.ViewEstudiante.as_view(), name='estudiante'),
    url(r'^profesor/$', views.Profesor.as_view(), name='profesor'),
    url(r'^administrador/$', views.Administrador.as_view(), name='administrador'),
    url('editar_estudiante/', views.editar_estudiante, name='editar_estudiante'),    
	url('guardar_estudiante/', views.guardar_estudiante, name='guardar_estudiante'),
	url('ver_ramos_estudiante/', views.ViewRamosEstudiante.as_view(), name='ver_ramos_estudiante'),
	url('filtrar_ramos_estudiante/', views.filtrar_ramos_estudiante, name='filtrar_ramos_estudiante'),
]