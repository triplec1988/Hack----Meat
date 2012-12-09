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
    desired_pickup = forms.DateField()


class CutForm(forms.Form):
    pork_shoulder = forms.ChoiceField(choices=PORK_SHOULDER, required=False, widget=forms.CheckboxSelectMultiple)
    pork_loin = forms.ChoiceField(choices=PORK_LOIN, required=False, widget=forms.CheckboxSelectMultiple)
    pork_belly = forms.ChoiceField(choices=PORK_BELLY, required=False, widget=forms.CheckboxSelectMultiple)
    pork_leg = forms.ChoiceField(choices=PORK_LEG, required=False, widget=forms.CheckboxSelectMultiple)
    pork_sausage = forms.ChoiceField(choices=PORK_SAUSAGE, required=False, widget=forms.CheckboxSelectMultiple)
    pork_other = forms.ChoiceField(choices=PORK_OTHER, required=False, widget=forms.CheckboxSelectMultiple)
    beef_rib = forms.ChoiceField(choices=BEEF_RIB, required=False, widget=forms.CheckboxSelectMultiple)
    beef_loin = forms.ChoiceField(choices=BEEF_LOIN, required=False, widget=forms.CheckboxSelectMultiple)
    beef_sirloin = forms.ChoiceField(choices=BEEF_SIRLOIN, required=False, widget=forms.CheckboxSelectMultiple)
    beef_round = forms.ChoiceField(choices=BEEF_ROUND, required=False, widget=forms.CheckboxSelectMultiple)
    beef_other = forms.ChoiceField(choices=BEEF_OTHER, required=False, widget=forms.CheckboxSelectMultiple)
    special_instructions = forms.CharField(required=False, widget=forms.Textarea)
