import requests

# Importer les données
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max"
response = requests.get(url)

if response.status_code == 200:  # Source existante
    data = response.json()

    # Vérifier si 'daily' est une liste
    if isinstance(data.get('daily'), list):
        for daily_data in data['daily']:
            date = daily_data.get('time', 'N/A')
            max_temp = daily_data.get('temperature_2m_max', 'N/A')
            min_temp = daily_data.get('temperature_2m_min', 'N/A')
            precipitation_sum = daily_data.get('precipitation_sum', 'N/A')
            wind_speed_max = daily_data.get('wind_speed_10m_max', 'N/A')

            print(f"Date: {date}")
            print(f"Température maximale: {max_temp}°C")
            print(f"Température minimale: {min_temp}°C")
            print(f"Somme des précipitations: {precipitation_sum} mm")
            print(f"Vitesse du vent maximale: {wind_speed_max} m/s")
            print("\n")

    else:
        date = data.get('daily', {}).get('time', 'N/A')
        max_temp = data.get('daily', {}).get('temperature_2m_max', 'N/A')
        min_temp = data.get('daily', {}).get('temperature_2m_min', 'N/A')
        precipitation_sum = data.get('daily', {}).get('precipitation_sum', 'N/A')
        wind_speed_max = data.get('daily', {}).get('wind_speed_10m_max', 'N/A')

        print(f"Date: {date}")
        print(f"Température maximale: {max_temp}°C")
        print(f"Température minimale: {min_temp}°C")
        print(f"Somme des précipitations: {precipitation_sum} mm")
        print(f"Vitesse du vent maximale: {wind_speed_max} m/s")

else:
    print("Erreur lors de la requête HTTP")

