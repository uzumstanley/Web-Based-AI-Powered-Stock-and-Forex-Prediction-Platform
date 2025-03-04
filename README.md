# GBP/USD Forex Prediction Web App

## 📌 Project Overview
This project is a **GBP/USD exchange rate prediction web application** built using **Flask, Streamlit, TensorFlow, and scikit-learn**. It fetches **live forex rates**, displays **historical data**, and predicts the **next 3 days** using an **LSTM-based deep learning model**.

## 🚀 Features
✅ Fetch **real-time GBP/USD exchange rate** via Open Exchange Rates API  
✅ Visualize **historical forex data** with interactive charts  
✅ Predict the **next 3 days** using a **trained LSTM model**  
✅ Deploy as a **Flask API** and **Streamlit UI**  

## 🛠️ Technologies Used
- **Python** (Backend & Data Processing)
- **Flask** (REST API for predictions)
- **Streamlit** (Frontend Web UI)
- **TensorFlow/Keras** (LSTM Model for time series forecasting)
- **scikit-learn** (Preprocessing & Scaling)
- **pandas & NumPy** (Data Handling)
- **matplotlib & seaborn** (Data Visualization)
- **Open Exchange Rates API** (Live forex data)

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/forex-prediction-webapp.git
cd forex-prediction-webapp
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Forex Dataset
Ensure you have a historical dataset (`forex_data.csv`) in the project directory.

### 4️⃣ Run Flask API (Backend)
```bash
python app.py
```

### 5️⃣ Run Streamlit UI (Frontend)
```bash
streamlit run ui.py
```

## 📊 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/latest`      | GET    | Returns the latest GBP/USD exchange rate |
| `/predict`     | GET    | Returns 3-day GBP/USD predictions |

## 🔮 Sample Predictions
```json
{
    "predictions": [
        {"date": "2025-02-26", "rate": 0.7896},
        {"date": "2025-02-27", "rate": 0.7885},
        {"date": "2025-02-28", "rate": 0.7874}
    ]
}
```

## 🚀 Future Improvements
- ✅ Improve model accuracy with hyperparameter tuning
- ✅ Deploy on **AWS/GCP/Heroku** for public access
- ✅ Integrate **news sentiment analysis** for better predictions
- ✅ Add **more currency pairs** for broader forecasting






