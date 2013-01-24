from django import forms
from django.core.validators import *
<<<<<<< HEAD
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

PROFILE_CHOICES = (
    ('FA', 'Farmer'),
    ('PR', 'Processor'),

    )

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class UserSignupForm(UserCreationForm):
	occupation = forms.ChoiceField(required=True, choices=PROFILE_CHOICES)

	def save(self, commit=False):
		user = super(UserSignupForm, self).save(commit=False)
		user.save()

		try:
			profile = user.get_profile()
		except:
			profile = UserProfile(user=user)

		profile.occupation = self.cleaned_data['occupation']
		profile.save()

	#class Meta(UserCreationForm.Meta):
	#	fields = ('username', 'email', 'first_name', 'last_name', )

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('occupation', )

class FarmerForm(forms.ModelForm):
	class Meta:
		model = Farmer
		fiels = ('farm_name')

class ProcessorForm(forms.ModelForm):
	class Meta:
		model = Processor
		fiels = ('plant_name')




=======


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60}))
>>>>>>> 689b49e40fb468291135292e8ac4970ff45d0f14
