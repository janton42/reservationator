import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from scheduler.models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from scheduler.forms import RegistrationForm

def index(request):
	
	return render(request, 'scheduler/index.html')

def vote(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	try:
		selected_choice = event.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'scheduler/date.html', {
			'event': event,
			'error_message': "Please choose at least one date.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('scheduler:details', args=(event_id,)))

def signup(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})
    elif request.method == 'POST':
    	form = RegistrationForm(request.POST)
    	if form.is_valid():
    		form.save()
    		return redirect('scheduler:index')
    	else:
    		form = RegistrationForm(request.POST)
    		return render(request, 'signup.html', {'form': form})

def updateUser(request):
	if request.method == 'GET':
		form = UserChangeForm()
		return render(request, '')

class EventCreate(LoginRequiredMixin, CreateView):
	model = Event
	fields = '__all__'
	success_url = '/scheduler/events'

class EventsListView(generic.ListView, LoginRequiredMixin):
	model = Event
	template_name = 'scheduler/events.html'

	def get_queryset(self):
		return Event.objects.filter(host=self.request.user)

class EventDelete(LoginRequiredMixin, DeleteView):
	model = Event
	success_url = '/scheduler/events'

class EventUpdate(LoginRequiredMixin, UpdateView):
	model = Event
	fields = ['name', 'place']
	success_url = '/scheduler/events'

class ChoiceView(generic.DetailView,LoginRequiredMixin):
	model = Choice
	template_name = 'scheduler/date.html'

	def get_queryset(self):
		return Choice.objects.all()

class ChoiceCreate(LoginRequiredMixin, CreateView):
	model = Choice
	fields = ['event', 'date']
	success_url = '/scheduler/events'

class DetailsView(generic.DetailView,LoginRequiredMixin):
	model = Event
	template_name = 'scheduler/details.html'

class ChoiceUpdate(LoginRequiredMixin, UpdateView):
	model = Choice
	fields = ['date']
	success_url = '/scheduler/events'

class ChoiceDelete(LoginRequiredMixin, DeleteView):
	model = Choice
	success_url = '/scheduler/events'

class ContactsListView(generic.ListView, LoginRequiredMixin):
	model = Contact
	template_name = 'scheduler/contacts.html'

	def get_queryset(self):
		return Contact.objects.filter(owner=self.request.user)