from django.contrib import admin
from scheduler.models import Profile, Event, Choice, Place

admin.site.register(Profile)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Choice)
