from django.db import models
import random
# Create your models here.

class Room(models.Model):
    name = models.TextField(max_length=100)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=True)


class Booked(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

