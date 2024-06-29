import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
@st.cache_data
def load_data():
    car_data = pd.read_csv('vehicles_us_df.csv')
    return car_data

# Configurar la página web con Streamlit
def main():
    st.title('Visualización de Datos de Vehículos')

    # Cargar datos
    car_data_df = load_data()
 
    st.header('Datos de Vehículos') # Mostrar tabla de datos inicialmente
    all_columns = car_data_df.columns.tolist() # Lista de todas las columnas

     # Checkbox para seleccionar columnas a mostrar
    selected_columns = []
    for column in all_columns:
        if st.checkbox(column):
            selected_columns.append(column)

    # Mostrar solo las columnas seleccionadas
    if selected_columns:
        st.write(car_data_df[selected_columns])
    
    st.header('Creación de los graficos') 

    with st.expander("Histograma de Precios"):    
        graf_button_hist = st.button('Construir histograma', key = 'graf_button_hist')
        if graf_button_hist:
            #st.write('Anuncio de ventas de coches')
            fig = px.histogram(car_data_df, x='price', nbins=50, title='Histograma de Precios de los Vehículos')
            fig.update_layout(xaxis_title='Precio', yaxis_title='Frecuencia')
            st.plotly_chart(fig, use_container_width = True)
    
    with st.expander("Gráfico de Barras de Año de Modelo"):
        graf_button_bar = st.button('Construir grafico de barras', key = 'graf_button_bar')
        if graf_button_bar:
            #st.write('Grafico de barras de Año de Modelo')
            fig = px.histogram(car_data_df, x='model_year', title='Cantidad de Vehículos por Año de Modelo')
            fig.update_layout(xaxis_title='Año del Modelo', yaxis_title='Cantidad de Vehículos')
            st.plotly_chart(fig, use_container_width = True)

    with st.expander("Kilometraje por Tipo de Vehículo"):
        graf_button_big = st.button('Construir grafico de barras', key = 'graf_button_big')
        if graf_button_big:
            #st.write('Gráfico de Cajas y Bigotes de Kilometraje por Tipo de Vehículo')
            fig = px.box(car_data_df, x='type', y='odometer', title='Distribución de Kilometraje por Tipo de Vehículo')
            fig.update_layout(xaxis_title='Tipo de Vehículo', yaxis_title='Kilometraje')
            st.plotly_chart(fig, use_container_width = True)

    with st.expander("Diagrama de Dispersiones de Precio vs. Kilometraje"):
        graf_button_dis = st.button('Construir grafico de dispersión', key = 'graf_button_dis')
        if graf_button_dis:
            fig = px.scatter(car_data_df, x='odometer', y='price', title='Relación entre Precio y Kilometraje',
                 labels={'odometer': 'Kilometraje', 'price': 'Precio'})
            st.plotly_chart(fig, use_container_width = True)

    with st.expander("Gráfico de Pastel de Tipo de Combustible"):
        graf_button_pas = st.button('Construir grafico de Pastel', key = 'graf_button_pas')
        if graf_button_pas:
            fig = px.pie(car_data_df, names='fuel', title='Proporción de Vehículos por Tipo de Combustible',
             labels={'fuel': 'Tipo de Combustible'}, color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig, use_container_width = True)

if __name__ == '__main__':
    main()