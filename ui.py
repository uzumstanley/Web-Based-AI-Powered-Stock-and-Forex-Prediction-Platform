import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Backend API URL
API_BASE_URL = "http://127.0.0.1:5000"

# Fetch latest forex rate
def get_latest_rate():
    response = requests.get(f"{API_BASE_URL}/latest").json()
    return response["latest_rate"]

# Fetch predictions
def get_predictions():
    response = requests.get(f"{API_BASE_URL}/predict").json()
    return response["predictions"]

# Load historical forex data
def load_forex_data():
    return pd.read_csv("forex_data.csv", index_col="Date", parse_dates=True)

# Streamlit UI
st.title("💹 GBP/USD Forex Predictor")
st.write("This application fetches live exchange rates, displays historical trends, and predicts the next 3 days.")

# Latest Forex Rate
st.header("📌 Latest Exchange Rate")
latest_rate = get_latest_rate()
st.metric(label="Current GBP/USD Rate", value=f"{latest_rate:.4f}")

# Historical Data Chart
st.header("📊 Historical Exchange Rate")
forex_data = load_forex_data()
st.line_chart(forex_data["Rate"])

# Predictions
st.header("🔮 3-Day Future Predictions")
predictions = get_predictions()

pred_dates = [pred["date"] for pred in predictions]
pred_rates = [pred["rate"] for pred in predictions]

st.table(pd.DataFrame({"Date": pred_dates, "Predicted Rate": pred_rates}))

# Plot predictions
fig, ax = plt.subplots()
ax.plot(pred_dates, pred_rates, marker="o", linestyle="dashed", color="red", label="Predicted GBP/USD")
ax.legend()
st.pyplot(fig)
