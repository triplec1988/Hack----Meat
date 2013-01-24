from django.core.validators import *
from cuts import *
from django import forms
from django.forms import ModelForm
from hackmeat.reservation.models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60}))


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ('status')


class Cut_FormForm(ModelForm):
    class Meta:
        model = Cut_Form
