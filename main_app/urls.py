from django.urls import path
from . import views

urlpatterns = [
	# example home path:
	path('', views.home, name='home'),
]