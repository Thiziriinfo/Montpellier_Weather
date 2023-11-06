
import requests
#Importer les donnée
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,wind_speed_10m_max"

response = requests.get(url)

if response.status_code == 200: #ressource existe
    data = response.json()
    print(data)
else:
    print("Erreur lors de la requête HTTP")

