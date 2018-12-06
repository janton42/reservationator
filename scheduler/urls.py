from django.urls import path 
from django.conf.urls import include
from . import views

app_name = 'scheduler'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.ChoiceView.as_view(), name='date'),
	path('<int:pk>/details/', views.DetailsView.as_view(), name='details'),
	path('<int:event_id>/vote/', views.vote, name='vote'),
	path('create/', views.create, name='create'),
	path('events/', views.EventsListView.as_view(), name='events'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]