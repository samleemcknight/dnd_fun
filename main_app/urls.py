from django.urls import path
from . import views

urlpatterns = [
	# example home path:
	path('', views.home, name='home'),
  path('characters/', views.characters, name="characters"),
]