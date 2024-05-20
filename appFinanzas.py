#Importa la librería streamlit y la nombra st

import streamlit as st


#st: librería
#write: método
#(): variables

import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import requests
import io

# URL del archivo CSV en tu repositorio de GitHub
url = 'https://raw.githubusercontent.com/tu-usuario/tu-repositorio/rama/path/al/archivo/df_sample.csv'

# Descargar el archivo CSV
response = requests.get(url)
response.raise_for_status()  # Asegúrate de que la solicitud fue exitosa

# Leer el archivo CSV en un DataFrame
my_large_df = pd.read_csv(io.StringIO(response.text))

# Función para convertir el DataFrame a CSV (según tu código original)
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

# Mostrar el DataFrame en Streamlit
st.dataframe(my_large_df)

# Botón para descargar el DataFrame como CSV
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='df_sample.csv',
    mime='text/csv',
)




col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")



chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

import plotly.graph_objects as go
import numpy as np

# Generar datos aleatorios
np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

# Crear la figura 3D
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

# Configurar el diseño de la figura
fig.update_layout(
    title='Gráfica 3D con valores aleatorios',
    scene=dict(
        xaxis_title='X AXIS',
        yaxis_title='Y AXIS',
        zaxis_title='Z AXIS'
    )
)

# Mostrar la figura en Streamlit
st.plotly_chart(fig)

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)




st.title("PISA Analisis :smile:") 

st.header('Tec de Monterrey')
st.subheader('Danna Ximena Medina Galvan :bar_chart:')

st.divider()

st.subheader('Calculadora de rentas de una casa')

st.write("¿Cuánto es el VPN de un pago mensual de una renta de una casa, si el arrendatario paga 12,000 durante 5 años?")
st.write("La tasa de descuento es del 6%")

mensualidad = st.number_input('Ingrese la mensualidad')
periodos = st.number_input('Ingrese el número de meses de rentas', 12, 60)

st.write('La mensualidad es ', mensualidad)

tasa_descuento = 0.06  # Tasa de descuento

vpn = sum([mensualidad / (1 + tasa_descuento) ** n for n in range(1, periodos + 1)])

st.write(f"El Valor Presente Neto de la renta de una casa que paga {mensualidad} al mes, considerando una tasa de {tasa_descuento} durante {periodos} meses es de **${vpn:,.2f}**.")

st.divider()

st.subheader('Calculadora para el retiro')
st.write("¿Cuánto necesito tener en mi cuenta de banco si me quiero retirar?")

pagomensual= st.number_input("¿Cuánto es el valor de tus gastos mensuales?")
tasa_rendimiento= 0.138

perpetuidad = (pagomensual * 12)/ tasa_rendimiento

st.markdown(f"Para obtener un ingreso de {pagomensual} al mes, necesitas tener invertirdo **${perpetuidad:,.2f}** a una tasa del {tasa_rendimiento} :sweat_smile:")

st.divider()

st.subheader('Calculadora Monto total de un crédito')


monto_prestamo = st.number_input("Ingresa el Monto de tu préstamo", 15000)
tasa_interes_anual = st.number_input("Ingresa la tasa de interés de tu préstamo",0.07)
periodos_credito = 5 
st.write(f"En número de periodos está preestablecido en {periodos_credito}")

tasa_anual = tasa_interes_anual
pago_anual = monto_prestamo * (tasa_anual / (1 - (1 + tasa_anual) ** -periodos_credito))
monto_total_pagado = pago_anual * periodos_credito

st.write(f"El monto total pagado por el crédito es: **${monto_total_pagado:,.2f}**")








