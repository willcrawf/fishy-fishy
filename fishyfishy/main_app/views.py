from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class FishCreate(LoginRequiredMixin, CreateView):
    model = Fish
    fields = ['breed','age','color','length','gender', 'notes']
    success_url = '/fishs/'
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fishs/'
  
# Define the home view
def home(request):
  return render(request, 'home.html')

@login_required
def fishs_index(request):
  fishs = Fish.objects.filter(user=request.user)
  return render(request, 'fishs/index.html', { 'fishs': fishs })

@login_required
def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fishs/detail.html', { 'fish': fish })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)