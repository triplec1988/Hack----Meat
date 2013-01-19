from django.db import models
from hackmeat.account.models import Processor, Farmer
from cuts import *

# Create your models here.

STATUS = (
    ('SU', 'Submitted'),
    ('CF', 'Confirmed'),
    ('PR', 'Processing'),
    ('CP', 'Complete'),
)

ANIMAL = (
    ('HOG', 'Hog'),
    ('COW', 'Cow'),
)


class Reservation(models.Model):
    farmer = models.ForeignKey(Farmer, related_name='farmers')
    processor = models.ForeignKey(Processor, related_name='processors')
    dropoff_time = models.DateTimeField()
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
    reservation = models.ForeignKey(Reservation, related_name='animal_reservations')
    animal_one = models.CharField(max_length=3, choices=ANIMAL, )
    animal_one_quantity = models.PositiveIntegerField()
    animal_two = models.CharField(max_length=3, choices=ANIMAL, blank=True, )
    animal_two_quantity = models.PositiveIntegerField(null=True, blank=True)


    def __unicode__(self):
        return u'{0} - {2}'.format(self.reservation, self.animal_one, self.animal_one_quantity, )


class Cut_Form(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='cut_reservations')
    pork_shoulder = models.CharField(max_length=3, choices=PORK_SHOULDER, blank=True, )
    pork_loin = models.CharField(max_length=3, choices=PORK_LOIN, blank=True, )
    pork_belly = models.CharField(max_length=3, choices=PORK_BELLY, blank=True, )
    pork_leg = models.CharField(max_length=3, choices=PORK_LEG, blank=True, )
    pork_sausage = models.CharField(max_length=3, choices=PORK_SAUSAGE, blank=True, )
    pork_other = models.CharField(max_length=3, choices=PORK_OTHER, blank=True, )
    beef_rib = models.CharField(max_length=3, choices=BEEF_RIB, blank=True, )
    beef_loin = models.CharField(max_length=3, choices=BEEF_LOIN, blank=True, )
    beef_sirloin = models.CharField(max_length=3, choices=BEEF_SIRLOIN, blank=True, )
    beef_round = models.CharField(max_length=3, choices=BEEF_ROUND, blank=True, )
    beef_other = models.CharField(max_length=3, choices=BEEF_OTHER, blank=True, )
    special_instructions = models.CharField(max_length=500, blank=True, )
