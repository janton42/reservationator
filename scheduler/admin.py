from django.contrib import admin
from scheduler.models import Profile, Event, EventInstance, Place

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(EventInstance)
admin.site.register(Place)

