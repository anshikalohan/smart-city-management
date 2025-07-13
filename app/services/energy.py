import os
import requests
from typing import Optional

def determine_region(lat: float, lon: float) -> Optional[str]:
    if (lat >= 26.0 and lat <= 32.0) and (lon >= 74.0 and lon <= 81.0):
        return "north"
    elif (lat >= 18.0 and lat <= 26.0) and (lon >= 68.0 and lon <= 76.0):
        return "west"
    elif (lat >= 8.0 and lat <= 20.0) and (lon >= 76.0 and lon <= 86.0):
        return "south"
    elif (lat >= 22.0 and lat <= 30.0) and (lon >= 88.0 and lon <= 97.0):
        return "northeast"
    return None

def get_energy_data(region: str) -> Optional[dict]:
    zone_mapping = {
        "north": "IN-NO",
        "west": "IN-WE",
        "south": "IN-SO",
        "northeast": "IN-NE"
    }
    
    zone = zone_mapping.get(region.lower())
    if not zone:
        return None
    
    api_key = os.getenv(f"ELECTRICITY_MAPS_{region.upper()}")
    if not api_key:
        return None
    
    try:
        url = f"https://api.electricitymap.org/v3/power-breakdown/latest?zone={zone}"
        headers = {"auth-token": api_key}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data for {zone}: {str(e)}")
        return None

def calculate_energy_metrics(energy_data: dict) -> float:
    if not energy_data:
        return 0.0
    
    total_production = sum(
        value for key, value in energy_data.get("powerProductionBreakdown", {}).items() 
        if isinstance(value, (int, float))
    )
    return round(total_production, 2)
