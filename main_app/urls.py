from django.urls import path
from . import views

urlpatterns = [
	# example home path:
	path('', views.home, name='home'),
  path('characters/', views.characters, name="characters"),
  path('races/', views.races, name="races"),
  path('races/<str:name>', views.race, name="show_race")
]