import uuid

from datetime import datetime

from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from phone_field import PhoneField
from localflavor.us.models import USStateField

class Event(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=400, help_text='Enter a name for your event')
	place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True)
	created_on = models.DateField(auto_now_add=True, null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name}'

class Choice(models.Model):
	event = models.ForeignKey('Event', on_delete=models.CASCADE)
	date = models.DateTimeField('time and date', null=True)
	votes = models.IntegerField(default=0)

	class Meta:
		ordering = ['date']

	def __str__(self):
		return f'{self.id} ({self.event.name})'

class Place(models.Model):
	name = models.CharField(max_length=400, blank=False, help_text='Enter a place name')
	street = models.CharField(max_length=400, blank=False, help_text='Enter the street and number')
	city = models.CharField(max_length=150, blank=False)
	state = USStateField()
	zipcode = models.CharField(max_length=5)

	CUISINE = (
		('1', 'American'),
		('2', 'Italian'),
		('3', 'Steakhouse'),
		('4', 'Seafood'),
		('5', 'French'),
		('6', 'Indian'),
		('7', 'Mexican'),
		('8', 'Japanese'),
		('9', 'British'),
		('10', 'Chinese'),
		('11', 'Spanish'),
		('12', 'Fusion/Eclectic'),
		('13', 'Barbecue'),
		('14', 'Greek'),
		('15', 'Tapas/Small Plates'),
		('16', 'Comfort Food'),
		('17', 'Burgers'),
		('18', 'Vegiterian/Vegan'),
		('19', 'Fish'),
		('20', 'Dessert'),
		('21', 'Burmese'),
		('22', 'Asian'),
		('23', 'Bar/Lounge/Bottle Service'),
		('24', 'Beer Garden'),
		('25', 'Bistro'),
		('26', 'Cajun'),
		('27', 'Californian'),
		('28', 'Cocktail Bar'),
		('29', 'Creole'),
		('30', 'Gastro Pub'),
		('31', 'Global/International'),
		('32', 'Latin/Spanish'),
		('33', 'Latin American'),
		('34', 'Mediterranean'),
		('35', 'Peruvian'),
		('36', 'Southwest'),
		('37', 'Tex-Mex'),
		('38', 'Wine Bar'),
		('39', 'Farm-to-Table'),
		)
	
	PRICE = (
		('1', '$'),
		('2', '$$'),
		('3', '$$$'),
		('4', '$$$$'),
		)

	pricequartile = models.CharField(max_length=1, choices=PRICE, blank=False)
	cuisine = models.CharField(max_length=2, choices=CUISINE, blank=False)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name}'

class Invitation(models.Model):
	event = models.ForeignKey('Event', on_delete=models.CASCADE)
	invitee = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'invitations'

	def __str__(self):
		return f'{self.id} ({self.event.name})'
