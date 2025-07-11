import os
import requests
import datetime

def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
    return None

def estimate_people_count(weather_data):
    if not weather_data:
        return None
        
    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["main"]
    hour = datetime.datetime.now().hour

    base = 50
    if 6 <= hour <= 9:
        base = 100
    elif 10 <= hour <= 17:
        base = 150
    elif 18 <= hour <= 21:
        base = 200

    if condition in ["Rain", "Snow", "Thunderstorm"]:
        base *= 0.5
    elif condition in ["Clear", "Clouds"]:
        base *= 1.2

    if temp < 10 or temp > 35:
        base *= 0.7
    elif 20 <= temp <= 30:
        base *= 1.1

    return int(base)
