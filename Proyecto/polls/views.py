from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question, Choice, InstanciaAsignatura,User, Estudiante, Asignatura
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
    

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ViewEstudiante(generic.ListView):
    model = Estudiante
    template_name = 'polls/estudiante.html'
 
    def get_queryset(self):        
        """Obtener el nombre del usuario con sesion iniciada y devolver el estudiante con el mismo nombre"""     

        return Estudiante.objects.filter(username = self.request.user.username)

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


















class Profesor(TemplateView):
	template_name = 'polls/profesor.html'

class Administrador(TemplateView):
	template_name = 'polls/administrador.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
