from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
from .models import  Profile, Estudiante, Carrera, MallaCurricular, Asignatura, InstanciaAsignatura, EstadoInscripcion, MatriculaMalla, InscripcionAsignatura

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')
    list_select_related = ('profile', )

    def get_role(self,instance):
    	if instance.profile.role!=None:
    		return instance.profile.ROLE_CHOICES[instance.profile.role-1][1]
    	else:
    		return '-'	
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Estudiante)
admin.site.register(Carrera)
admin.site.register(MallaCurricular)
admin.site.register(Asignatura)
admin.site.register(InstanciaAsignatura)
admin.site.register(EstadoInscripcion)
admin.site.register(MatriculaMalla)
admin.site.register(InscripcionAsignatura)
