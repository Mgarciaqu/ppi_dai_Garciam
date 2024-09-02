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

# Vista principal
def index(request):
    return render(request, 'index.html')

# Lista de productos
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Detalle de producto
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Perfil del usuario (requiere login)
@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

# Carrito de compras (requiere login)
@login_required
def cart(request):
    return render(request, 'cart.html')

# Filtro de precios usando NumPy
def price_filter(min_price, max_price):
    prices = np.array([product.price for product in Product.objects.all()])
    filtered_products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
    return filtered_products

# Información sobre el creador de la aplicación
def about_view(request):
    return render(request, 'about.html', {
        'creator_name': 'Nombre del Creador',
        'creator_email': 'email@dominio.com',
        'description': 'Esta aplicación fue creada para...'
    })

# Política de privacidad
def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

# Registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Conversor de moneda
def currency_converter_view(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        conversion_rate = 0.85  # Ejemplo: 1 USD = 0.85 EUR
        result = amount * conversion_rate
        return render(request, 'currency_converter.html', {'result': result})
    return render(request, 'currency_converter.html')

# Generador de número aleatorio
def random_number_view(request):
    if request.method == 'POST':
        min_value = int(request.POST.get('min', 0))
        max_value = int(request.POST.get('max', 100))
        result = random.randint(min_value, max_value)
        return render(request, 'random_number.html', {'result': result})
    return render(request, 'random_number.html')

# Consulta de clima (datos fijos)
def weather_view(request):
    weather_data = {
        'city': 'Bogotá',
        'temperature': 18,
        'condition': 'Nublado'
    }
    return render(request, 'weather.html', {'weather': weather_data})

# Funcionalidades básicas sin registro
def basic_functionality_1(request):
    # Lógica de la primera funcionalidad básica
    return render(request, 'basic_functionality_1.html')

def basic_functionality_2(request):
    # Lógica de la segunda funcionalidad básica
    return render(request, 'basic_functionality_2.html')

def basic_functionality_3(request):
    # Lógica de la tercera funcionalidad básica
    return render(request, 'basic_functionality_3.html')

# Funcionalidades avanzadas con registro
@login_required
def advanced_functionality_1(request):
    # Lógica de la primera funcionalidad avanzada
    return render(request, 'advanced_functionality_1.html')

@login_required
def advanced_functionality_2(request):
    # Lógica de la segunda funcionalidad avanzada
    return render(request, 'advanced_functionality_2.html')

@login_required
def advanced_functionality_3(request):
    # Lógica de la tercera funcionalidad avanzada
    return render(request, 'advanced_functionality_3.html')

