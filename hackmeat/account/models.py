from django.db import models
from hackmeat.reservation.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

PROFILE_CHOICES = (
    ('FA', 'Farmer'),
    ('PR', 'Processor'),

    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profiles')
    occupation = models.CharField(max_length=2, choices=PROFILE_CHOICES)

def save(self, *args, **kwargs):
    if not self.pk:
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.pk = existing.pk
        except UserProfile.DoesNotExist:
            pass
            models.Model.save(self, *args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            profile, created = UserProfile.objects.get_or_create(user=instance)
        except:
            pass

post_save.connect(create_user_profile, sender=User)

class Farmer(models.Model):
    user_profile = models.OneToOneField(UserProfile, related_name='farmers')
    farm_name = models.CharField(max_length=30)

class Processor(models.Model):
    user_profile = models.OneToOneField(UserProfile, related_name='processors')
    plant_name = models.CharField(max_length=30)


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
