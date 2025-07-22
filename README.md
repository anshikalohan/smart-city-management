# Smart City Dashboard 🏙️

Welcome to the **Smart City Dashboard** – a comprehensive urban insights platform designed to provide real-time data on traffic congestion, energy optimization, public safety, and crowd density.

## 🌟 Key Features

*   **Real-time Traffic Insights**: Integrates with the TomTom API to provide live traffic speeds and uses Machine Learning (Polynomial Regression) to predict future congestion levels.
*   **Energy Optimization**: Connects to the Electricity Maps API to track regional energy production and consumption across India.
*   **Public Safety Alerts**: Aggregates localized public safety news using NewsData.io.
*   **Crowd Density Estimation**: Analyzes live weather conditions (via OpenWeather) and time-of-day metrics to estimate crowd flow.
*   **Interactive Mapping**: Features a responsive, dynamic Leaflet.js and OpenStreetMap integration for precise geographic visualization.

## 🏗️ Architecture

The project follows a clean, modular MVC (Model-View-Controller) architecture built on Flask:

```text
smart_city_project/
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── routes.py             # Controller definitions
│   ├── services/
│   │   ├── traffic.py        # TomTom Geocoding & Traffic Logic
│   │   ├── weather.py        # OpenWeather & Crowd Logic
│   │   ├── news.py           # Public Safety News Aggregator
│   │   └── energy.py         # Electricity Maps Integration
│   └── models/
│       └── traffic_model.py  # Polynomial Regression Traffic Predictor
├── static/
│   ├── style.css             # Premium Glassmorphism UI Styles
│   └── script.js             # Geolocation & Leaflet.js Logic
├── templates/
│   └── dashboard.html        # Semantic HTML Structure
└── run.py                    # Application Entry Point
```

## 🎨 UI/UX Design

The frontend is completely free of external CSS frameworks like Tailwind or Bootstrap. Instead, it relies on a **Premium Vanilla CSS** architecture featuring:
- High-performance Glassmorphism (blurred backdrops and translucent panels)
- Smooth micro-animations and loading states
- Responsive CSS Grid layouts
- Google 'Inter' Typography

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- API Keys for TomTom, OpenWeather, NewsData, and Electricity Maps

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anshikalohan/smart-city-management.git
   cd smart-city-management
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Configure Environment Variables:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   TOMTOM_API_KEY=your_key_here
   OPENWEATHER_API_KEY=your_key_here
   NEWS_API_KEY=your_key_here
   ELECTRICITY_MAPS_IN_NO=your_key_here
   ELECTRICITY_MAPS_IN_WE=your_key_here
   ELECTRICITY_MAPS_IN_SO=your_key_here
   ELECTRICITY_MAPS_IN_NE=your_key_here
   ```

4. Run the Application:
   ```bash
   python run.py
   ```
   Access the dashboard at `http://127.0.0.1:5000`.

---
*Developed by Anshika Lohan*
