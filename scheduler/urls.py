from django.urls import path 
from django.conf.urls import include
from . import views

app_name = 'scheduler'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>/details/', views.DetailsView.as_view(), name='details'),
	path('<int:event_id>/vote/', views.vote, name='vote'),
]

urlpatterns += [
	path('events/', views.EventsListView.as_view(), name='events'),
	path('event/create', views.event_create, name='event_create'),
	path('event/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete'),
	path('event/<int:pk>/update', views.EventUpdate.as_view(), name='event_update'),
]

urlpatterns += [
	path('<int:pk>', views.ChoiceView.as_view(), name='date'),
	path('choices/<int:event_id>/create', views.choice_create, name='choice_create'),
	path('choices/<int:pk>/update', views.ChoiceUpdate.as_view(), name='choice_update'),
	path('choices/<int:pk>/delete', views.ChoiceDelete.as_view(), name='choice_delete'),
]

urlpatterns += [
	path('invitations_received/', views.InvitationsReceivedListView.as_view(), name='invitations_received'),
	path('invitations_sent/', views.InvitationsSentListView.as_view(), name='invitations_sent'),
	path('invitation/<int:event_id>/create', views.invitation_create, name='invitation_create'),
	path('invitation/<int:pk>/update', views.InvitationUpdate.as_view(), name='invitation_update'),
	path('invitation/<int:pk>/delete', views.InvitationDelete.as_view(), name='invitation_delete'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]