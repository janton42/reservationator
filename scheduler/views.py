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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from scheduler.forms import *
from django import forms

def index(request):
	
	return render(request, 'scheduler/index.html')

@login_required
def vote(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	if Voter.objects.filter(event_id=event_id, user_id=request.user.id).exists():
		return render(request, 'scheduler/warning.html', {
			'event': event,
			'error_message': "You've already voted."
			})
	try:
		selected_choice = event.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'scheduler/warning.html', {
			'event': event,
			'error_message': "you didn't vote."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		v = Voter(user=request.user, event=event)
		v.save()
		return HttpResponseRedirect(reverse('scheduler:invitations_received'))

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

# ----Event Views---------------------------------------------
class EventsListView(generic.ListView, LoginRequiredMixin):
	model = Event
	template_name = 'scheduler/events.html'

	def get_queryset(self):
		return Event.objects.filter(host=self.request.user)

class EventUpdate(LoginRequiredMixin, UpdateView):
	model = Event
	fields = ['name', 'place']
	success_url = '/scheduler/events'

# class EventCreate(LoginRequiredMixin, CreateView):
# 	model = Event
# 	fields = '__all__'
# 	success_url = '/scheduler/events'

@login_required
def event_create(request):
	if request.method == 'POST':
		form = EventCreationForm(request.POST)
		if form.is_valid():
			event_create = form.save(commit=False)
			event_create.host = request.user
			event_create.save()
			return redirect('scheduler:events')
	else:
		form = EventCreationForm()
	return render(request, 'scheduler/event_form.html', {'form': form})

class EventDelete(LoginRequiredMixin, DeleteView):
	model = Event
	success_url = '/scheduler/events'


# ----Choice Views---------------------------------------------
class ChoiceView(generic.DetailView,LoginRequiredMixin):
	model = Choice
	template_name = 'scheduler/date.html'

	def get_queryset(self):
		return Choice.objects.all()

class ChoiceUpdate(LoginRequiredMixin, UpdateView):
	model = Choice
	fields = ['date']
	success_url = '/scheduler/events'

# class ChoiceCreate(LoginRequiredMixin, CreateView):
# 	model = Choice
# 	fields = ['event', 'date', 'time']
# 	success_url = '/scheduler/events'

@login_required
def choice_create(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	if request.method == 'POST':
		form = ChoiceCreationForm(request.POST)
		if form.is_valid():
			choice_create = form.save(commit=False)
			choice_create.event = event
			choice_create.save()
			return redirect('scheduler:events')
	else:
		form = ChoiceCreationForm()
	return render(request, 'scheduler/choice_form.html', {'form': form})

class ChoiceDelete(LoginRequiredMixin, DeleteView):
	model = Choice
	success_url = '/scheduler/events'



class DetailsView(generic.DetailView,LoginRequiredMixin):
	model = Event
	template_name = 'scheduler/details.html'

# ----Invitation Views------------------------------------------
class InvitationsReceivedListView(generic.ListView, LoginRequiredMixin):
	model = Invitation
	template_name = 'scheduler/invitations_received.html'

	def get_queryset(self):
		return Invitation.objects.filter(invitee=self.request.user)

class InvitationsSentListView(generic.ListView, LoginRequiredMixin):
	model = Invitation
	template_name = 'scheduler/invitations_sent.html'

	def get_queryset(self):
		return Invitation.objects.all()

class InvitationUpdate(LoginRequiredMixin, UpdateView):
	model = Invitation
	fields = ['event', 'invitee']
	success_url = '/scheduler/invitations_sent'

class InvitationCreate(LoginRequiredMixin, CreateView):
	model = Invitation
	fields = '__all__'
	success_url = '/scheduler/invitations_sent'

class InvitationDelete(LoginRequiredMixin, DeleteView):
	model = Invitation
	success_url = '/scheduler/invitations_sent'
