from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
from django.views.generic import ListView
from django.http import HttpResponse


class FishCreate(CreateView):
    model = Fish
    fields = '__all__'
    success_url = '/fish/'

class FishUpdate(UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'
  
# Define the home view
def home(request):
  return render(request, 'home.html')

def fish_index(request):
  return render(request, 'fish/index.html', { 'fish': 'fish' })