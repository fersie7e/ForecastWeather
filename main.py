import streamlit as st
import plotly.express as px
from controller import get_data

st.title("Tiempo en los proximos dias")
place = st.text_input("Ciudad: ")
days = st.slider("Dias", min_value=1, max_value=5, help="Seleccione el numero "
                                                        "de dias a mostrar")
option = st.selectbox("Seleccione los datos a mostrar: ",
                       ("Temperatura",
                         "Cielo"))
st.subheader(f"{option} para los proximos {days} dias en {place}")

d, t = get_data(place, days, option)


figure = px.line(x=d, y=t, labels={"x":"Fecha", "y": "Temperaturas ºC"})
st.plotly_chart()
