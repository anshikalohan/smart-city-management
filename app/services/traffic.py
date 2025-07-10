import os
import requests

def get_place_name(lat, lon):
    url = f"https://api.tomtom.com/search/2/reverseGeocode/{lat},{lon}.json?key={os.getenv('TOMTOM_API_KEY')}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'addresses' in data and len(data['addresses']) > 0:
                return data['addresses'][0]['address']['freeformAddress']
    except Exception as e:
        print(f"Error in reverse geocode: {e}")
    return "Unknown Location"

def get_coordinates_from_place(place_name):
    url = f"https://api.tomtom.com/search/2/geocode/{place_name}.json?key={os.getenv('TOMTOM_API_KEY')}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]['position']
                return result['lat'], result['lon']
    except Exception as e:
        print(f"Error in geocode: {e}")
    return None, None

def get_traffic_data(lat, lon):
    traffic_url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={os.getenv('TOMTOM_API_KEY')}&point={lat},{lon}"
    try:
        response = requests.get(traffic_url, timeout=5)
        if response.status_code == 200:
            traffic_data = response.json()
            if 'flowSegmentData' in traffic_data:
                return traffic_data['flowSegmentData']
    except Exception as e:
        print(f"Error fetching traffic: {e}")
    return None
