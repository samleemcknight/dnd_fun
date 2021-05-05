from django.shortcuts import render
import requests

# Create your views here.

def home(request):
  # races = requests.get('https://www.dnd5eapi.co/api/races')
  # races = races.json()
  # race_info = []
  # for x in races['results']:
  #   race = requests.get(f"https://www.dnd5eapi.co/api/races/{x['index']}")
  #   race = race.json()
  #   race_info.append(race)
  # context = {
  #   "race_info": race_info
  # }
  return render(request, 'index.html')

def characters(request):
  return render(request, 'characters.html')

def races(request):
  return render(request, 'races/index.html')

def race(request, name):
  return render(request, 'races/show.html')