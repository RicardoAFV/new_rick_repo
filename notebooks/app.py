import streamlit as st
import pandas as pd
import plotly.express as px
ruta = "C:/Users/Ricardo/new_rick_repo/vehicles_us.csv"
vehicles_us = pd.read_csv(ruta)
# Título o encabezado principal de la app
st.header('Análisis de anuncios de venta de coches')
hist_button = st.button('Construir histograma')
if hist_button:
    # Mostrar mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear histograma con Plotly
    fig = px.histogram(vehicles_us, x="odometer")

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    fig2 = px.scatter(vehicles_us, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

show_hist = st.checkbox('Mostrar histograma de kilometraje')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles_us, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión: Precio vs Kilometraje')

if show_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    fig2 = px.scatter(vehicles_us, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)