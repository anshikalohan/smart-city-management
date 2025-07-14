from flask import render_template, request, current_app as app
import datetime

from .services.traffic import get_coordinates_from_place, get_traffic_data, get_place_name
from .services.weather import get_weather_data, estimate_people_count
from .services.news import get_public_safety_news
from .services.energy import determine_region, get_energy_data, calculate_energy_metrics
from .models.traffic_model import traffic_model

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    congestion_data = None
    place_name = None
    future_hour = None
    error = None
    estimated_people = None
    energy_consumption = None
    region = None
    public_safety_news = []

    if request.method == "POST":
        place_name_input = request.form.get("place_name")
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        future_hour = request.form.get("future_hour")

        if place_name_input and not (latitude and longitude):
            latitude, longitude = get_coordinates_from_place(place_name_input)
            if latitude is None or longitude is None:
                error = "Could not find coordinates for the given place name."

        if latitude and longitude and not error:
            try:
                lat_float = float(latitude)
                lon_float = float(longitude)
                
                congestion_data = get_traffic_data(lat_float, lon_float)
                place_name = get_place_name(lat_float, lon_float)
                
                region = determine_region(lat_float, lon_float)
                if region:
                    energy_data_response = get_energy_data(region)
                    if energy_data_response:
                        energy_consumption = calculate_energy_metrics(energy_data_response)

                public_safety_news = get_public_safety_news(place_name=place_name)

                weather_data = get_weather_data(lat_float, lon_float)
                if weather_data:
                    estimated_people = estimate_people_count(weather_data)
                
                if congestion_data and future_hour:
                    try:
                        future_hour = int(future_hour)
                        current_hour = datetime.datetime.now().hour
                        if future_hour < 0 or future_hour > 23:
                            error = "Please enter a valid hour (0-23)."
                        elif future_hour < current_hour:
                            error = "Cannot predict traffic for past hours. Please enter a future hour."
                        else:
                            current_speed = congestion_data.get("currentSpeed", 0)
                            predicted_speed, speed_reduction, congestion_score = traffic_model.predict_future_traffic(current_speed, future_hour)
                            prediction = {
                                "future_hour": future_hour,
                                "predicted_speed": predicted_speed,
                                "speed_reduction": speed_reduction,
                                "congestion_score": congestion_score
                            }
                    except ValueError:
                        error = "Invalid input for future hour. Please enter a number between 0 and 23."
            except ValueError:
                error = "Invalid latitude/longitude values. Please enter valid numbers."
    else:
        public_safety_news = get_public_safety_news(place_name="India")

    return render_template("dashboard.html",
                         prediction=prediction,
                         congestion_data=congestion_data,
                         place_name=place_name,
                         error=error,
                         estimated_people=estimated_people,
                         energy_consumption=energy_consumption,
                         region=region,
                         public_safety_news=public_safety_news)
