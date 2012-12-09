from django import forms
from django.core.validators import *
from cuts import *


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
    pork_shoulder = forms.ChoiceField(choices=PORK_SHOULDER, required=False, widget=forms.RadioSelect)
    pork_loin = forms.ChoiceField(choices=PORK_LOIN, required=False, widget=forms.RadioSelect)
    pork_belly = forms.ChoiceField(choices=PORK_BELLY, required=False, widget=forms.RadioSelect)
    pork_leg = forms.ChoiceField(choices=PORK_LEG, required=False, widget=forms.RadioSelect)
    pork_sausage = forms.ChoiceField(choices=PORK_SAUSAGE, required=False, widget=forms.RadioSelect)
    pork_other = forms.ChoiceField(choices=PORK_OTHER, required=False, widget=forms.RadioSelect)
    beef_rib = forms.ChoiceField(choices=BEEF_RIB, required=False, widget=forms.RadioSelect)
    beef_loin = forms.ChoiceField(choices=BEEF_LOIN, required=False, widget=forms.RadioSelect)
    beef_sirloin = forms.ChoiceField(choices=BEEF_SIRLOIN, required=False, widget=forms.RadioSelect)
    beef_round = forms.ChoiceField(choices=BEEF_ROUND, required=False, widget=forms.RadioSelect)
    beef_other = forms.ChoiceField(choices=BEEF_OTHER, required=False, widget=forms.RadioSelect)
    special_instructions = forms.CharField(required=False, widget=forms.Textarea)
