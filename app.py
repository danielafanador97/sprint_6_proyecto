import streamlit as st
import pandas as pd
import plotly as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Histograma de anuncion de venta de carros')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header('Grafico de dispersion')

disp_button = st.button('Construir grafico de dispersion')

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafioco de dispersion del precio de los vehiculos a la venta')

    # crear un grafico de dispersion
    fig_2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
