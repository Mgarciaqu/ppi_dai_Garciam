from django.contrib import admin
from django.urls import path, include
from django.urls import path
from micael import views

urlpatterns = [
    # Otras rutas existentes...
    path('about/', views.about_view, name='about'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

urlpatterns = [
    # Otras rutas existentes...
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
]

