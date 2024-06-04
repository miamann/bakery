from django.shortcuts import render
from .models import Product, Recipe

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def index(request):
    products = Product.objects.all()
    recipe = Recipe.objects.first() 
    return render(request, 'index.html', {'products': products, 'recipe': recipe})