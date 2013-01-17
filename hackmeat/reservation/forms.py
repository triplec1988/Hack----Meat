from django import forms, ModelForm
from django.core.validators import *
from cuts import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60}))


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('farmers.first_name', 'farmers.last_name', 'famers.farm_name',
                  'dropoff_time', )


class Animal_ReservationForm(ModelForm):
    class Meta:
        model = Animal_ReservationForm


class Cut_FormForm(ModelForm):
    class Meta:
        model = Cut_Form
        widgets = {
            ('pork_shoulder', 'pork_loin', 'pork_belly', 'pork_leg', 
             'pork_sausage', 'pork_other', 'beef_rib', 'beef_loin', 
             'beef_sirloin', 'beef_round', 'beef_other': 
              CheckboxSelectMultiple), ('special_instructions': 
              Textarea(attrs={'cols': 60}))
        }
