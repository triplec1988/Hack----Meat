from django.db import models
from hackmeat.account.models import Processor, Farmer

# Create your models here.

STATUS = (
    ('SU', 'Submitted'),
    ('CF', 'Confirmed'),
    ('PR', 'Processing'),
    ('CP', 'Complete'),
)


class Reservation(models.Model):
    farmer = models.ForeignKey(Farmer, related_name='farmers')
    processor = models.ForeignKey(Processor, related_name='processors')
    instruction = models.TextField()
    dropoff_time = models.DateTimeField()
    pickup_time = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS)


class Blackout(models.Model):
    processor = models.ForeignKey(Processor, related_name='closed')
    start_time = models.DateField()
    end_time = models.DateField()
    reason = models.CharField(max_length=140)


class Animal_Reservation(models.Model):
    reservation = models.ForeignKey('Reservation', related_name='reservations')
    animal = models.ForeignKey('Animal', related_name='animal_type')
    animal_quantity = models.PositiveIntegerField()
    cut = models.CharField(max_length=100)


class Animal(models.Model):
    name = models.CharField(max_length=50)
