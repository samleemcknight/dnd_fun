from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  return render(request, 'index.html')

def characters(request):
  return render(request, 'characters.html')

def races(request):
  return render(request, 'races/index.html')

def race(request, name):
  race = requests.get(f"https://www.dnd5eapi.co/api/races/{name}")
  race = race.json()
  subrace = []
  if race['subraces']:
    subrace = requests.get(f"https://www.dnd5eapi.co/api/subraces/{race['subraces'][0]['index']}")
    subrace = subrace.json()
  context = {
    "race_info": race,
    "subrace": subrace
  }
  return render(request, 'races/show.html', context)