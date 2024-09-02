from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegistroForm
from .models import ActividadUsuario
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
import geopandas as gpd
from io import BytesIO
import base64

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            registrar_actividad(user, "Registro de nuevo usuario")
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            registrar_actividad(user, "Cambio de contraseña")
            return redirect('perfil')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambiar_contrasena.html', {'form': form})

def registrar_actividad(user, accion):
    actividad = ActividadUsuario(user=user, accion=accion)
    actividad.save()

def vista_publica_1(request):
    return render(request, 'publica_1.html')

def vista_publica_2(request):
    return render(request, 'publica_2.html')

def vista_publica_3(request):
    return render(request, 'publica_3.html')

@login_required
def vista_avanzada_1(request):
    return render(request, 'avanzada_1.html')

@login_required
def vista_avanzada_2(request):
    return render(request, 'avanzada_2.html')

@login_required
def vista_avanzada_3(request):
    return render(request, 'avanzada_3.html')

def numpy_view(request):
    arreglo = np.array([1, 2, 3])
    suma = np.sum(arreglo)
    registrar_actividad(request.user, "Análisis con NumPy")
    return render(request, 'numpy_analysis.html', {'suma': suma})

def pandas_view(request):
    df = pd.read_csv('ruta/al/archivo.csv')
    primeros = df.head()
    registrar_actividad(request.user, "Análisis con Pandas")
    return render(request, 'pandas_analysis.html', {'primeros': primeros.to_html()})

def matplotlib_view(request):
    plt.figure(figsize=(5, 5))
    plt.plot([1, 2, 3], [4, 5, 6])
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    registrar_actividad(request.user, "Gráfico con Matplotlib")
    return render(request, 'matplotlib_plot.html', {'image_base64': image_base64})

def scipy_view(request):
    resultado, error = quad(lambda x: x**2, 0, 1)
    registrar_actividad(request.user, "Cálculo con SciPy")
    return render(request, 'scipy_analysis.html', {'resultado': resultado})

def geopandas_view(request):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world_plot = world.plot()
    buf = BytesIO()
    world_plot.figure.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    registrar_actividad(request.user, "Mapa con GeoPandas")
    return render(request, 'geopandas_map.html', {'image_base64': image_base64})
