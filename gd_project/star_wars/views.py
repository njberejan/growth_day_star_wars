from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Planet, Person, Starship, Vehicle, Species
import swapi


# Create your views here.
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['planets'] = Planet.objects.all()
        context['starships'] = Starship.objects.all()
        context['vehicles'] = Vehicle.objects.all()
        context['species'] = Species.objects.all()
        return context
