from django.db import models
from hackmeat.reservation.models import *

# Create your models here.


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    farm_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField(max_length=10)

    def __unicode__(self):
        return u'{0} - {3}'.format(self.first_name, self.last_name, self.farm_name, self.zipcode)


class Processor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    plant_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField(max_length=10)
    resource = models.ManyToManyField('Resource')
    animal_spec = models.CharField(max_length=140)
    cut_spec = models.CharField(max_length=140)
    capacity = models.PositiveIntegerField()

    def __unicode__(self):
        return u'{0} - {3}'.format(self.first_name, self.last_name, self.plant_name, self.zipcode)


class Resource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Fee(models.Model):
    processor = models.ForeignKey('Processor', related_name='processor_fees')
    slaughter = models.BooleanField()
    slaughter_fee = models.DecimalField(max_digits=10, decimal_places=2)
    packaging = models.BooleanField()
    packaging_fee = models.DecimalField(max_digits=10, decimal_places=2)
    processing = models.BooleanField()
    processing_fee = models.DecimalField(max_digits=10, decimal_places=2)
