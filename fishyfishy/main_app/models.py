from django.db import models
# Import the reverse function
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Fish(models.Model):  # Note that parens are optional if not inheriting from another class
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    length = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    notes = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})