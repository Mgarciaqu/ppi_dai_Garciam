from django.shortcuts import render, redirect
from django.contrib.auth import login
from .formularios import FormularioCreacionUsuario

def registro(request):
    if request.method == 'POST':
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = FormularioCreacionUsuario()
    return render(request, 'registro.html', {'formulario': formulario})

