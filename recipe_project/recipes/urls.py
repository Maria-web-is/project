
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),  # Landing page for unauthenticated users
    path('home/', views.home, name='home'),  # Home page for authenticated users
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_recipe, name='add_recipe'),
    
]
