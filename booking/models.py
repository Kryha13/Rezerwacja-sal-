from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms
from rezerwacja.settings import DATE_INPUT_FORMATS

# Create your models here.


def validate_date(booked_from):
    if booked_from < timezone.now().date:
        raise ValidationError("Date cannot be in the past")


class Room(models.Model):
    name = models.TextField(max_length=100, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=True)


class Booked(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booked_from = models.DateField(null=True, validators=[validate_date])
    booked_to = models.DateField(null=True, validators=[validate_date])

    def save(self, *args, **kwargs):
        # check for items that have an overlapping start date
        booked_items_overlapping_start = Booked.objects.filter(booked_from__gte=self.booked_from, booked_from__lte=self.booked_to).exists()

        # check for items that have an overlapping end date
        booked_items_overlapping_end = Booked.objects.filter(booked_to__gte=self.booked_from, booked_to__lte=self.booked_to).exists()

        # check for items that envelope this item
        booked_items_enveloping = Booked.objects.filter(booked_from__lte=self.booked_from, booked_to__gte=self.booked_to).exists()

        overlapping_dimension_items_present = booked_items_overlapping_start or booked_items_overlapping_end or booked_items_enveloping

        if overlapping_dimension_items_present:
            raise forms.ValidationError('Dates are overlapping with existing bookings')
        else:
            super(Booked, self).save(*args, **kwargs)  # Call the "real" save() method.

