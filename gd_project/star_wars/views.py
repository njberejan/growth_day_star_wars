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
        queryset = swapi.get_all('people')
        context['people'] = queryset.items
        return context
