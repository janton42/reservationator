from django.contrib import admin
from scheduler.models import *

admin.site.register(Invitation)
admin.site.register(Contact)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Choice)
