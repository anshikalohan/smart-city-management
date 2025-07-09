import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class TrafficModel:
    def __init__(self):
        self.model = None
        self.poly = None
        self.KAGGLE_DATASET = "kaggle_traffic_data.csv"
        self._train()
        
    def _load_kaggle_data(self):
        if os.path.exists(self.KAGGLE_DATASET):
            df = pd.read_csv(self.KAGGLE_DATASET)
            if all(col in df.columns for col in ["Hour", "Speed"]):
                return df[["Hour", "Speed"]]
        return None

    def _load_traffic_data(self):
        historical_times = np.array([0, 6, 9, 12, 15, 18, 21, 24]).reshape(-1, 1)
        historical_speeds = np.array([40, 35, 25, 30, 28, 20, 22, 38])

        kaggle_data = self._load_kaggle_data()
        if kaggle_data is not None:
            historical_times = np.vstack([historical_times, kaggle_data["Hour"].values.reshape(-1, 1)])
            historical_speeds = np.hstack([historical_speeds, kaggle_data["Speed"].values])

        return historical_times, historical_speeds

    def _train(self):
        X, y = self._load_traffic_data()
        self.poly = PolynomialFeatures(degree=3)
        X_poly = self.poly.fit_transform(X)
        self.model = LinearRegression()
        self.model.fit(X_poly, y)

    def predict_future_traffic(self, current_speed, future_hour):
        future_hour = future_hour % 24
        predicted_speed = self.model.predict(self.poly.transform([[future_hour]]))[0]
        speed_reduction = round(current_speed - predicted_speed, 2)
        congestion_score = round((1 - (predicted_speed / current_speed)) * 100, 2) if current_speed > 0 else 100
        return round(predicted_speed, 2), speed_reduction, congestion_score

traffic_model = TrafficModel()
