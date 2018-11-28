import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from scheduler.models import Event, EventInstance, Place
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
	
# def index(request):


# 	return render(request, 'index.html')

class IndexView(generic.ListView):
	template_name = 'scheduler/index.html'
	context_object_name = 'event_list'

	def get_queryset(self):
		return Event.objects.all().order_by('name')

class InstanceView(generic.DetailView):
	model = EventInstance
	template_name = 'scheduler/date.html'

	def get_queryset(self):
		return EventInstance.objects.all()

class ResultsView(generic.DetailView):
	model = Event
	template_name = 'scheduler/results.html'

def vote(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	try:
		selected_date = event.instance_set.get(pk=request.POST['eventinstance'])
	except (KeyError, EventInstance.DoesNotExist):
		return render(request, 'scheduler/date.html', {
			'event': event,
			'error_message': "You didn't vote.",
			})
	else:
		selected_date.votes += 1
		selected_date.save()
		return HttpResponseRedirect(reverse('scheduler:results', args=(event_id)))