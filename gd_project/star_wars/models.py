from django.db import models

# Create your models here.


class Planet(models.Model):
    climate = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    gravity = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    orbital_period = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=100)
    surface_water = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

class Person(models.Model):
    birth_year = models.CharField(max_length=100)
    eye_color = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    homeworld = models.CharField(max_length=100, null=True)
    mass = models.CharField(max_length=100)
    skin_color = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    edited = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class Starship(models.Model):
    MGLT = models.CharField(max_length=100)
    cargo_capacity = models.CharField(max_length=100)
    consumables = models.CharField(max_length=100)
    cost_in_credits = models.CharField(max_length=100)
    crew = models.CharField(max_length=100)
    hyperdrive_rating = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_atmosphering_speed = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    starship_class = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class Vehicle(models.Model):
    cargo_capacity = models.CharField(max_length=100)
    consumables = models.CharField(max_length=100)
    cost_in_credits = models.CharField(max_length=100)
    created = models.CharField(max_length=100)
    crew = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_atmosphering_speed = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    vehicle_class = models.CharField(max_length=100)


class Species(models.Model):
    average_height = models.CharField(max_length=100)
    average_lifespan = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    eye_colors = models.CharField(max_length=100)
    hair_colors = models.CharField(max_length=100)
    homeworld = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    skin_colors = models.CharField(max_length=100)
    url = models.CharField(max_length=100)