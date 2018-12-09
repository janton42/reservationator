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

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]