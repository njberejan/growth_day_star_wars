from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Planet, Person, Starship, Vehicle, Species
import swapi

def download_data(self):
    people_queryset = swapi.get_all('people').items
    planet_queryset = swapi.get_all('planets').items
    species_queryset = swapi.get_all('species').items
    starship_queryset = swapi.get_all('starships').items
    vehicle_queryset = swapi.get_all('vehicles').items

    for planet in planet_queryset:
        dbplanet = Planet(
            climate = planet.climate,
            diameter = planet.diameter,
            gravity = planet.gravity,
            name = planet.name,
            orbital_period = planet.orbital_period,
            rotation_period = planet.rotation_period,
            surface_water = planet.surface_water,
            terrain = planet.terrain,
            url = planet.url
        )
        dbplanet.save()
    print('PLANETS SAVED')

    for person in people_queryset:
        dbperson = Person(
            birth_year = person.birth_year,
            eye_color = person.eye_color,
            gender = person.gender,
            hair_color = person.hair_color,
            height = person.height,
            homeworld = person.homeworld,
            mass = person.mass,
            name = person.name,
            skin_color = person.skin_color,
            url = person.url
        )
        dbperson.save()
    print('PEOPLE SAVED')

    for species in species_queryset:
        dbspecies = Species(
            average_height = species.average_height,
            average_lifespan = species.average_lifespan,
            classification = species.classification,
            designation = species.designation,
            eye_colors = species.eye_colors,
            hair_colors = species.hair_colors,
            homeworld = species.homeworld,
            language = species.language,
            name = species.name,
            skin_colors = species.skin_colors,
            url = species.url
        )
        dbspecies.save()
    print('SPECIES SAVED')

    for starship in starship_queryset:
        dbstarship = Starship(
            MGLT = starship.MGLT,
            cargo_capacity = starship.cargo_capacity,
            consumables = starship.consumables,
            cost_in_credits = starship.cost_in_credits,
            crew = starship.crew,
            hyperdrive_rating = starship.hyperdrive_rating,
            length = starship.length,
            manufacturer = starship.manufacturer,
            max_atmosphering_speed = starship.max_atmosphering_speed,
            model = starship.model,
            name = starship.name,
            passengers = starship.passengers,
            starship_class = starship.starship_class,
            url = starship.url
        )
        dbstarship.save()
    print('STARSHIPS SAVED')

    for vehicle in vehicle_queryset:
        dbvehicle = Vehicle(
            cargo_capacity = vehicle.cargo_capacity,
            consumables = vehicle.consumables,
            cost_in_credits = vehicle.cost_in_credits,
            created = vehicle.created,
            crew = vehicle.crew,
            length = vehicle.length,
            manufacturer = vehicle.manufacturer,
            max_atmosphering_speed = vehicle.max_atmosphering_speed,
            model = vehicle.model,
            name = vehicle.name,
            passengers = vehicle.passengers,
            url = vehicle.url,
            vehicle_class = vehicle.vehicle_class
        )
        dbvehicle.save()
    print('VEHICLES SAVED')


# Create your views here.
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        queryset = swapi.get_all('people')
        context['people'] = queryset.items
        return context
