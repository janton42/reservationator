from django.urls import path 
from django.conf.urls import include
from . import views

app_name = 'scheduler'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.ChoiceView.as_view(), name='date'),
	path('<int:pk>/details/', views.DetailsView.as_view(), name='details'),
	path('<int:event_id>/vote/', views.vote, name='vote'),
]

urlpatterns += [
	path('events/', views.EventsListView.as_view(), name='events'),
	path('events/create', views.EventCreate.as_view(), name='event_create'),
	path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete'),
	path('events/<int:pk>/update', views.EventUpdate.as_view(), name='event_update'),
]

urlpatterns += [
	path('choices/create', views.ChoiceCreate.as_view(), name='choice_create'),
	path('choices/<int:pk>/update', views.ChoiceUpdate.as_view(), name='choice_update'),
	path('choices/<int:pk>/delete', views.ChoiceDelete.as_view(), name='choice_delete'),
]

urlpatterns += [
	path('contacts/', views.ContactsListView.as_view(), name='contacts'),
	path('contacts/create', views.ContactCreate.as_view(), name='contact_create'),
	path('contacts/<int:pk>/update', views.ContactUpdate.as_view(), name='contact_update'),
	path('contacts/<int:pk>/delete', views.ContactDelete.as_view(), name='contact_delete'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]