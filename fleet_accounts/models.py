from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Sacco(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField(null=True)
    sacco_base = models.ForeignKey(Sacco, related_name='sacco_base')

    def __str__(self):
        return self.first_name


class Owner(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField(null=True)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    make = models.CharField(max_length=30, unique=True)
    model = models.CharField(max_length=30, unique=True)
    plate_number = models.IntegerField(unique=True)
    year = models.DateTimeField(null=True)
    owner = models.ForeignKey(Owner, related_name='owner')

    def __str__(self):
        return self.model


class Crew(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField(null=True)
    vehicle_base = models.ForeignKey(Vehicle, related_name='vehicle_base')

    def __str__(self):
        return self.first_name
