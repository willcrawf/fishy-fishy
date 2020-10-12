from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('fishs/', views.fishs_index, name='index'),
  path('fishs/create/', views.FishCreate.as_view(), name='fishs_create'),
  path('fishs/<int:fish_id>/', views.fish_detail, name='detail'),
  path('accounts/signup/', views.signup, name='signup'),

#   path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
#   path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
]