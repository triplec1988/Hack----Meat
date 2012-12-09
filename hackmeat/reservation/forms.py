from django import forms
from django.core.validators import *

ANIMALS = (
    ('P', 'Pigs'),
    ('C', 'Cattle'),
)


class ReservationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    farm_name = forms.CharField(max_length=100)
    animal_type_one = forms.ChoiceField(choices=ANIMALS)
    animal_quantity_one = forms.IntegerField()
    animal_type_two = forms.ChoiceField(choices=ANIMALS, required=False)
    animal_quantity_two = forms.IntegerField(required=False)
    dropoff = forms.DateTimeField()
    pickup = forms.DateTimeField()


class CutForm(forms.Form):
	pork_shoulder
