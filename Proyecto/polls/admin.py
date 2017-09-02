from django.contrib import admin

# Register your models here.
from .models import  Estudiante, Carrera, MallaCurricular, Asignatura, InstanciaAsignatura, EstadoInscripcion, MatriculaMalla, InscripcionAsignatura



admin.site.register(Estudiante)
admin.site.register(Carrera)
admin.site.register(MallaCurricular)
admin.site.register(Asignatura)
admin.site.register(InstanciaAsignatura)
admin.site.register(EstadoInscripcion)
admin.site.register(MatriculaMalla)
admin.site.register(InscripcionAsignatura)
