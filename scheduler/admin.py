from django.contrib import admin
from scheduler.models import *

class InvitationAdmin(admin.ModelAdmin):
	list_display = ('id', 'event', 'invitee', 'created_on')

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'city', 'pricequartile', 'cuisine')

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'host', 'place', 'created_on')

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'date', 'votes')

admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Choice, ChoiceAdmin)
