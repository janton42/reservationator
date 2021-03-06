from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
			)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		email = self.cleaned_data['email']

		if commit:
			user.save()

			return user

class ChoiceCreationForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = (
			'date',
			'time',
			)
		widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}

class EventCreationForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = (
			'name',
			'place',
			)

class InvitationCreationForm(forms.ModelForm):
	class Meta:
		model = Invitation
		fields = (
			'invitee',
			)