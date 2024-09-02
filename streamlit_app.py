import streamlit as st
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celuya.configuracion')
django.setup()

st.title("Celuya!")
st.write("Bienvenido a la tienda de celulares en línea.")
