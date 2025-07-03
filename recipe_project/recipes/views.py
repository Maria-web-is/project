

from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages




@login_required
def home(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Link recipe to current user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()

    recipes = Recipe.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'recipes/home.html', {'form': form, 'recipes': recipes})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    recipes = Recipe.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'registration/dashboard.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect('dashboard')
          
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})
 

def landing_page(request):
    return render(request, 'landing.html')
