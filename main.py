import streamlit as st
import plotly.express as px
from controller import get_data


# Add title, text input, slider, select box, and subheader
st.title("Tiempo en los proximos dias")
place = st.text_input("Ciudad: ")
days = st.slider("Dias", min_value=1, max_value=5, help="Seleccione el numero "
                                                        "de dias a mostrar")
option = st.selectbox("Seleccione los datos a mostrar: ",
                       ("Temperatura",
                         "Cielo"))
st.subheader(f"{option} para los proximos {days} dias en {place}")

if place:
    # Get the data from the API
    filtered_data = get_data(place, days)

    if option == "Temperatura":
        temperaturas = [dict["main"]["temp"] for dict in filtered_data]
        fechas = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=fechas, y=temperaturas,
                         labels={"x":"Fecha", "y": "Temperaturas ºC"})
        st.plotly_chart(figure)

    if option == "Cielo":
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        images= {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                 "Rain": "images/rain.png", "Snow": "images/snow.png"}
        image_paths = [images[condition] for condition in sky_condition]
        st.image(image_paths, width=150)