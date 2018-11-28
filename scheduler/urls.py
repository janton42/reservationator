from django.urls import path 
from django.conf.urls import include
from . import views

app_name = 'scheduler'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.InstanceView.as_view(), name='date'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:event_id>/vote/', views.vote, name='vote'),
]