import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text
    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
        
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    correoElectronico = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre + self.apellidoPaterno + self.apellidoMaterno

class Carrera(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.nombre

class MallaCurricular(models.Model):
    carrera = models.ForeignKey(Carrera)
    version = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.version
        
class Asignatura(models.Model):
    mallaCurricular = models.ForeignKey(MallaCurricular)
    nombre = models.CharField(max_length=50)
    maxAlumnos = models.IntegerField(default=50)
    
    def __unicode__(self):
        return self.nombre
        
class InstanciaAsignatura(models.Model):
    SELSEM = (
        ('1', 'Primer semestre'),
        ('2', 'Segundo Semestre'),
    )
    asignatura = models.ForeignKey(Asignatura)
    alumnosInscritos = models.IntegerField(default=50)
    anio = models.CharField(max_length=4)
    semestre = models.CharField(max_length=1, choices=SELSEM)
    profesor = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.anio + self.semestre

class EstadoInscripcion(models.Model):
    SELINS = (
        ('I', 'Inscrito'),
        ('N', 'No inscrito'),
    )
    estado = models.CharField(max_length=1, choices=SELINS)
    
    def __unicode__(self):
        return self.estado
        
class MatriculaMalla(models.Model):
    mallaCurricular = models.ForeignKey(MallaCurricular)
    estudiante = models.ForeignKey(Estudiante)
    asignaturasAprobadas = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.asignaturasAprobadas

class InscripcionAsignatura(models.Model):
    SELAS = (
        ('A', 'Aprobado'),
        ('P', 'Pendiente'),
        ('R', 'Reprobado')
    )
    estudiante = models.ForeignKey(Estudiante)
    instancia = models.ForeignKey(InstanciaAsignatura)
    estadoInscripcion = models.ForeignKey(EstadoInscripcion)
    estadoFinal = models.CharField(max_length=1, choices=SELAS)
    notaFinal = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.asignaturasAprobadas
        
