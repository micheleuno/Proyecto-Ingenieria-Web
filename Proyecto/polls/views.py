from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question, Choice, InstanciaAsignatura,User, Estudiante, Asignatura, InscripcionAsignatura, MatriculaMalla, Carrera, MallaCurricular
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from django.forms import ModelForm
# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    model = InstanciaAsignatura

class ViewEstudiante(LoginRequiredMixin, generic.ListView):
    model = Estudiante
    template_name = 'polls/estudiante.html'
 
    def get_queryset(self):        
        """Obtener el nombre del usuario con sesion iniciada y devolver el estudiante con el mismo nombre"""     

        return Estudiante.objects.filter(username = self.request.user.username)

class ViewRamosEstudiante(LoginRequiredMixin, generic.ListView):
    model = InscripcionAsignatura
    template_name = 'polls/ver_ramos_estudiante.html'
 
    def get_queryset(self):
        obj_estudiante = Estudiante.objects.get(username = self.request.user.username)
        lista = InscripcionAsignatura.objects.filter(estudiante=obj_estudiante.id)
        return lista

class Inscripciones:
    def __init__(self):
        self.carrera = ''
        self.clave = ''
        self.nombre = ''
        self.anno = ''
        self.semestre = ''
        self.estado = ''


def filtrar_ramos_estudiante(request):
    obj_estudiante = Estudiante.objects.get(username = request.user.username)
    lista = InscripcionAsignatura.objects.filter(estudiante=obj_estudiante.id)
    lista_inscripciones = []
    """var_carrera = request.POST['carrera']"""
    var_anno = request.POST['anno']
    var_semestre = request.POST['semestre'] 
    var_estado = request.POST['estado'] 
    var_asignatura = request.POST['asignatura'] 
    for obj in lista:
        ins_asig = InstanciaAsignatura.objects.get(id=obj.instancia.id)
        asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id)
        malla= MatriculaMalla.objects.get(id=asignatura.mallaCurricular.id)
        """ asignatura=MallaCurricular.objects.get(id=malla.mallaCurricular.id)"""
        
        """ carrera= Carrera.objects.get(id=mallac.carrera)"""
           
        inscripcion = Inscripciones()
        
        """inscripcion.carrera = carrera """  
        inscripcion.nombre = asignatura.nombre
        inscripcion.anno = ins_asig.anio
        inscripcion.semestre = ins_asig.semestre
        inscripcion.estado = obj.estadoFinal

        if(obj.estadoFinal=='A'):
        	inscripcion.estado='Aprobado'
        if(obj.estadoFinal=='P'):
        	inscripcion.estado='Pendiente'
        if(obj.estadoFinal=='R'):
        	inscripcion.estado='Reprobado'

       
        #filtro
        if((inscripcion.anno == var_anno or var_anno == '') and ((inscripcion.nombre).lower() == (var_asignatura).lower() or var_asignatura == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and ((inscripcion.estado).lower() == (var_estado).lower() or var_estado == '')):
            lista_inscripciones.append(inscripcion)
    if(len(lista_inscripciones)==0):  
        inscripcion.nombre = "No se encontraron resultados"
        inscripcion.anno = ""
        inscripcion.semestre = ""
        inscripcion.estado = ""
        lista_inscripciones.append(inscripcion)

    context = {
        'usuario': obj_estudiante,
        'lista_inscripciones': lista_inscripciones,
       """ 'carrera' : var_carrera,"""
        'anno' : var_anno,
        'semestre' : var_semestre,
        'estado' : var_estado,
        'asignatura' : var_asignatura

    }
    return render(request, 'polls/ver_ramos_estudiante.html', context)

def editar_estudiante(request):
    estudiante2 = Estudiante.objects.get(username = request.user.username)
    context = {
        'estudiante': estudiante2
    }
    return render(request, 'polls/editar_estudiante.html', context)


def guardar_estudiante(request):

    obj_estudiante = Estudiante.objects.get(username=request.user.username)
    obj_estudiante.direccion=request.POST['direccion']
    obj_estudiante.correoElectronico=request.POST['correo']
    obj_estudiante.telefono=request.POST['telefono']
    obj_estudiante.save()
    context = {
        'estudiante': obj_estudiante
    }
   
    return render(request, 'polls/guardar_estudiante.html', context)





class Profesor(LoginRequiredMixin,TemplateView):
	template_name = 'polls/profesor.html'


def filtrar_ramos_profesor(request):
	obj_instancia_asignatura = InstanciaAsignatura.objects.filter(profesor = request.user.first_name+" "+request.user.last_name)
	lista_asignaturas = []


	if 'carrera' in request.POST:
		var_carrera = request.POST['carrera']
	else:
		var_carrera = ""

	if 'anno' in request.POST:
		var_anno = request.POST['anno']
	else:
		var_anno = ""

	if 'semestre' in request.POST:
		var_semestre = request.POST['semestre']
	else:
		var_semestre = ""
	if 'carrera' in request.POST:

		var_asignatura = request.POST['asignatura']
	else:
		var_asignatura = ""	

	for obj in obj_instancia_asignatura:
		inscripcion = Inscripciones()
		obj_asignatura = Asignatura.objects.get(id=obj.asignatura.id)
		obj_malla = MallaCurricular.objects.get(id=obj_asignatura.mallaCurricular.id)
		obj_carrera = Carrera.objects.get(id=obj_malla.carrera.id)
		inscripcion.nombre = obj_asignatura.nombre
		inscripcion.anno = obj.anio
		inscripcion.semestre = obj.semestre
		inscripcion.carrera = obj_carrera.nombre
		if((inscripcion.anno == var_anno or var_anno == '') and ((inscripcion.nombre).lower() == (var_asignatura).lower() or var_asignatura == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and ((inscripcion.carrera).lower() == (var_carrera).lower() or var_carrera == '')):
			lista_asignaturas.append(inscripcion)
	if(len(lista_asignaturas)==0):
		inscripcion.nombre = "No se encontraron resultados"
		inscripcion.anno = ""
		inscripcion.semestre = ""
		inscripcion.carrera = ""
		lista_asignaturas.append(inscripcion)	
	context = {
       
        'lista_inscripciones': lista_asignaturas,
        'anno' : var_anno,
        'semestre' : var_semestre,
        'nombre' : var_asignatura,
        'carrera' : var_carrera
    }

	return render(request, 'polls/ver_ramos_profesor.html', context)





class Administrador(LoginRequiredMixin,TemplateView):
	template_name = 'polls/administrador.html'