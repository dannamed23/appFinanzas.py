#Importa la librería streamlit y la nombra st

import streamlit as st


#st: librería
#write: método
#(): variables

st.title("Ejercicios de Finanzas :symbols:") 

st.header('Materia Ingeniería Financiera')
st.subheader('Aldo Emmanuel Medina Galván :alien:')

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








