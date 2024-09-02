from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('publica-1/', views.vista_publica_1, name='publica_1'),
    path('publica-2/', views.vista_publica_2, name='publica_2'),
    path('publica-3/', views.vista_publica_3, name='publica_3'),
    path('avanzada-1/', views.vista_avanzada_1, name='avanzada_1'),
    path('avanzada-2/', views.vista_avanzada_2, name='avanzada_2'),
    path('avanzada-3/', views.vista_avanzada_3, name='avanzada_3'),
    path('numpy/', views.numpy_view, name='numpy_view'),
    path('pandas/', views.pandas_view, name='pandas_view'),
    path('matplotlib/', views.matplotlib_view, name='matplotlib_view'),
    path('scipy/', views.scipy_view, name='scipy_view'),
    path('geopandas/', views.geopandas_view, name='geopandas_view'),
]
