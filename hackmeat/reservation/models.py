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

    def __unicode__(self):
        return u'{0} - {3}'.format(self.farmer.farm_name, self.processor.plant_name, self.dropoff_time, self.status, )


class Blackout(models.Model):
    processor = models.ForeignKey(Processor, related_name='closed')
    start_time = models.DateField()
    end_time = models.DateField()
    reason = models.CharField(max_length=140)

    def __unicode__(self):
        return u'{0} - {2}'.format(self.processor, self.start_time, self.end_time, )


class Animal_Reservation(models.Model):
    reservation = models.ForeignKey('Reservation', related_name='reservations')
    animal = models.ForeignKey('Animal', related_name='animal_type')
    animal_quantity = models.PositiveIntegerField()
    cut = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{0} - {2}'.format(self.reservation, self.animal, self.animal_quantity, )


class Animal(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'{0}'.format(self.name, )
