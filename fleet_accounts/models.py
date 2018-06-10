from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Sacco(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30, unique=True)
    sacco_logo = models.ImageField(
        upload_to='profile_pictures/sacco_logo', default='/static/img/logo-placeholder.jpg')

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField(null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/supervisor', default='/static/img/placeholder.png')
    sacco_base = models.ForeignKey(
        Sacco, related_name='sacco_base')

    def __str__(self):
        return self.first_name


class Owner(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField(null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/owner', default='/static/img/placeholder.png')

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
    profile_picture = models.ImageField(
        upload_to='profile_pictures/crew', default='/static/img/placeholder.png')

    def __str__(self):
        return self.first_name
