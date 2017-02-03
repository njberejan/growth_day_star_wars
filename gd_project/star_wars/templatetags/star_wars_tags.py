from django import template
from star_wars.models import Person, Planet, Starship, Vehicle, Species

register = template.Library()

"""http://stackoverflow.com/questions/3513990/django-rendering-inclusion-tag-from-a-view"""

@register.inclusion_tag('people.html')
def show_people():
    people = Person.objects.all()
    return { 'people' : people }

@register.inclusion_tag('planets.html')
def show_planets():
    planets = Planet.objects.all()
    return { 'planets' : planets }

@register.inclusion_tag('starships.html')
def show_starships():
    starships = Starship.objects.all()
    return { 'starships' : starships }


@register.inclusion_tag('vehicles.html')
def show_vehicles():
    vehicles = Vehicle.objects.all()
    return { 'vehicles' : vehicles }


@register.inclusion_tag('species.html')
def show_species():
    species = Species.objects.all()
    return { 'species' : species }
