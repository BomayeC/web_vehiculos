import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    #escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #crear un histograma
    fig = px.histogram(car_data, x='odometer')

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True)