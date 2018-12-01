from datetime import datetime

from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from phone_field import PhoneField
from localflavor.us.models import USStateField


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = PhoneField(blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Event(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=400, help_text='Enter a name for your event')
	place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True)

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
	PRICE = (
		('1', '$'),
		('2', '$$'),
		('3', '$$$'),
		('4', '$$$$'),
		)

	price_quartile = models.CharField(max_length=1, choices=PRICE, blank=False)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name}'
