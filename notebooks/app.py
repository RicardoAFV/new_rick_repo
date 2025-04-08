import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
ruta = "vehicles_us.csv"
vehicles_us = pd.read_csv(ruta)

# Título de la app
st.header('Análisis de anuncios de venta de coches')

# Histograma con checkbox
if st.checkbox('Mostrar histograma de kilometraje'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles_us, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión con checkbox
if st.checkbox('Mostrar gráfico de dispersión: Precio vs Kilometraje'):
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    fig2 = px.scatter(vehicles_us, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
# Botón: Histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches (botón)')
    fig = px.histogram(vehicles_us, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón: Gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje (botón)')
    fig2 = px.scatter(vehicles_us, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)