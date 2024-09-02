import random 
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import geopandas as gpd
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def cart(request):
    return render(request, 'cart.html')

def price_filter(min_price, max_price):
    prices = np.array([product.price for product in Product.objects.all()])
    return products[(prices >= min_price) & (prices <= max_price)]

def about_view(request):
    return render(request, 'about.html', {
        'creator_name': 'Nombre del Creador',
        'creator_email': 'email@dominio.com',
        'description': 'Esta aplicación fue creada para...'
    })

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Función para la conversión de monedas
def currency_converter_view(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        conversion_rate = 0.85  # Ejemplo: 1 USD = 0.85 EUR
        result = amount * conversion_rate
        return render(request, 'currency_converter.html', {'result': result})
    return render(request, 'currency_converter.html')

# Función para generar un número aleatorio
def random_number_view(request):
    if request.method == 'POST':
        min_value = int(request.POST.get('min', 0))
        max_value = int(request.POST.get('max', 100))
        result = random.randint(min_value, max_value)
        return render(request, 'random_number.html', {'result': result})
    return render(request, 'random_number.html')

# Función para consultar el clima (datos fijos)
def weather_view(request):
    weather_data = {
        'city': 'Bogotá',
        'temperature': 18,
        'condition': 'Nublado'
    }
    return render(request, 'weather.html', {'weather': weather_data})
