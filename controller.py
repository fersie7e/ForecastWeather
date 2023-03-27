import requests

API_KEY = "b6bf71f5f0eba52bb82b427bdbd3124f"
def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days # Se toman 8 mediciones al dia por eso esta linea
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperatura":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Cielo":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Cielo"))