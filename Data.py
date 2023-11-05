
import requests
#Importer les donnée
url = "https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,wind_speed_10m_max"

response = requests.get(url)

if response.status_code == 200: #ressource existe
    data = response.json()
    print(data)
else:
    print("Erreur lors de la requête HTTP")

