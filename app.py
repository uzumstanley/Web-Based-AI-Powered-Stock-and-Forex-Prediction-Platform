import numpy as np
import pandas as pd
import requests
import tensorflow as tf
from flask import Flask, jsonify
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load trained LSTM model
model = tf.keras.models.load_model("forex_lstm_model.h5")

# Open Exchange Rates API Key
API_KEY = "304ab1c9f84945b5b8543520bbb07ae7"

# Function to fetch latest GBP/USD rate
def get_latest_forex_rate():
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    response = requests.get(url).json()
    return response["rates"]["GBP"] / response["rates"]["USD"]

# Function to generate future predictions
def predict_future():
    # Load historical data
    forex_data = pd.read_csv("forex_data.csv", index_col="Date", parse_dates=True)
    
    # Prepare data for prediction
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(forex_data["Rate"].values.reshape(-1, 1))

    last_60_days = scaled_data[-60:]  # Take last 60 days as input
    future_days = 3
    predicted_rates = []

    for _ in range(future_days):
        X_input = last_60_days.reshape(1, 60, 1)
        predicted_scaled = model.predict(X_input)
        predicted_real = scaler.inverse_transform(predicted_scaled.reshape(-1, 1))[0, 0]

        predicted_rates.append(predicted_real)
        last_60_days = np.append(last_60_days[1:], predicted_scaled, axis=0)  # Rolling forecast

    # Format output
    predictions = []
    for i in range(future_days):
        date = (datetime.today() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        predictions.append({"date": date, "rate": round(predicted_rates[i], 4)})

    return predictions

# API Endpoints
@app.route("/latest", methods=["GET"])
def latest_rate():
    return jsonify({"latest_rate": get_latest_forex_rate()})

@app.route("/predict", methods=["GET"])
def predict():
    return jsonify({"predictions": predict_future()})

if __name__ == "__main__":
    app.run(debug=True)
