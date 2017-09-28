import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm

# Create your models here.
@python_2_unicode_compatible 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
class Estudiante(models.Model):
    username = models.CharField(max_length=50, unique=True, null=True)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20,null = True)
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    correoElectronico = models.CharField(max_length=50)

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class MallaCurricular(models.Model):
    carrera = models.ForeignKey(Carrera)
    version = models.CharField(max_length=50)    
    def __str__(self):
        return self.carrera.nombre
        
class Asignatura(models.Model):
    mallaCurricular = models.ForeignKey(MallaCurricular)
    nombre = models.CharField(max_length=50)
    maxAlumnos = models.IntegerField(default=50)
    
    def __str__(self):
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
    
    def __str__(self):
        return self.asignatura.nombre+" "+self.anio +" "+ self.semestre+" Semestre"

class EstadoInscripcion(models.Model):
    SELINS = (
        ('I', 'Inscrito'),
        ('N', 'No inscrito'),
    )
    estado = models.CharField(max_length=1, choices=SELINS)
    
    def __str__(self):
        return self.estado
        
class MatriculaMalla(models.Model):
    mallaCurricular = models.ForeignKey(MallaCurricular)
    estudiante = models.ForeignKey(Estudiante)
    asignaturasAprobadas = models.IntegerField(default=0)
    
    def __int__(self):
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
        
class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3  
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=False, blank=False, default=1)

    

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()       
