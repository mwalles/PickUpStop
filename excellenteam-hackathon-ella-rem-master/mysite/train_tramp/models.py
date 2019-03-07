from django.db import models
from django.urls import  reverse
from .paths import *
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    # destination = models.IntegerField(choices=(tuple([(i, (name)) for i, name in enumerate(path_1)])), default = 0)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    num = models.IntegerField()
    places_to_travel = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.phone

    def get_absolute_url(self):
        return reverse("Person:detail", args=(self.id,))


class Consumers (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name + self.phone

    def get_absolute_url(self):
        return reverse("Consumers:detail", args=(self.id,))
