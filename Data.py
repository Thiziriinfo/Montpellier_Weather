import requests

# Importer les données
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_direction_10m_dominant"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Vérifier si 'daily' est une liste
    if isinstance(data.get('daily'), list):
        for daily_data in data['daily']:
            date = daily_data.get('time', 'N/A')
            max_temp = daily_data.get('temperature_2m_max', 'N/A')
            min_temp = daily_data.get('temperature_2m_min', 'N/A')
            precipitation = daily_data.get('precipitation_sum', 'N/A')
            wind_direction = daily_data.get('wind_direction_10m_dominant', 'N/A')

            # Affichage des informations pour chaque jour
            print(f"Date : {date}")
            print(f"Température maximale : {max_temp}°C")
            print(f"Température minimale : {min_temp}°C")
            print(f"Précipitations : {precipitation} mm")
            print(f"Direction du vent dominante : {wind_direction}")
    else:
        # 'daily' est un dictionnaire, pas une liste
        date = data.get('daily', {}).get('time', 'N/A')
        max_temp = data.get('daily', {}).get('temperature_2m_max', 'N/A')
        min_temp = data.get('daily', {}).get('temperature_2m_min', 'N/A')
        precipitation = data.get('daily', {}).get('precipitation_sum', 'N/A')
        wind_direction = data.get('daily', {}).get('wind_direction_10m_dominant', 'N/A')

        # Affichage des informations pour un seul jour
        print(f"Date : {date}")
        print(f"Température maximale : {max_temp}°C")
        print(f"Température minimale : {min_temp}°C")
        print(f"Précipitations : {precipitation} mm")
        print(f"Direction du vent dominante : {wind_direction}")
else:
    print("Erreur lors de la requête HTTP")




