# 📊 End-to-End Time Series Forecasting System with API

## 🚀 Overview

This project implements a complete **end-to-end time series forecasting system** that predicts the next **8 weeks of sales for each state** using historical data.

The system covers the full pipeline:
- Data preprocessing  
- Feature engineering  
- Model training & comparison  
- Automatic model selection  
- Deployment via a REST API  

---

## 🎯 Objective

Build a **production-ready forecasting system** that:

- Trains multiple forecasting algorithms  
- Compares and selects the best model  
- Exposes predictions via a REST API  
- Follows a real backend service structure  


---

## 📊 Dataset

- Source: Provided Excel dataset  
- Contains historical **state-wise sales data**

---

## 🧹 Data Preprocessing

- Handled missing values using **forward fill (ffill)**
- Resampled data to ensure **weekly consistency**
- Ensured proper datetime indexing

---

## ⚙️ Feature Engineering

Created time-based features to capture temporal patterns:

- Lag features: `t-1`, `t-7`, `t-30`  
- Rolling statistics: mean & standard deviation  
- Month extraction  
- Time-series aware train-validation split (no leakage)

---

## 🤖 Models Implemented

The system trains and compares:

- **SARIMA (Statistical Model)**  
- **Facebook Prophet (Trend + Seasonality)**  
- **XGBoost (Feature-based ML)**  
- **LSTM (Deep Learning sequence model)**  

---

## 📈 Model Selection

- Evaluation metric: **RMSE (Root Mean Squared Error)**
- Best model automatically selected based on performance
- **SARIMA achieved the lowest RMSE and was deployed**

---

## 💾 Model Saving

- Models saved using **pickle format (.pkl)**
- Due to size constraints, a subset of states is included for demo
- System is designed to scale to all states

---

## ⚡ API Deployment

Built using **FastAPI**

### Endpoint:
GET /predict?state=<STATE>&steps=<N>


### Example:

### Output:

```json
{
  "state": "California",
  "forecast": [values...]
}
