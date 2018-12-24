from django.contrib import admin
from scheduler.models import Contact, Event, Choice, Place

admin.site.register(Contact)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Choice)
