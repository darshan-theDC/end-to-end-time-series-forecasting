from fastapi import FastAPI
from app.utils import load_model

app = FastAPI()

AVAILABLE_STATES = ["Arizona", "California", "Florida", "Kentucky", "Virginia", "Washington"]

# cache to store loaded models
MODEL_CACHE = {}


@app.get("/")
def home():
    return {"message": "Forecast API running"}

@app.get("/predict")
def predict(state: str, steps: int = 8):
    
    if state not in AVAILABLE_STATES:
        return {"error": "State not available"}
    
    # ✅ load model from cache OR disk
    if state in MODEL_CACHE:
        model = MODEL_CACHE[state]
    else:
        model = load_model(state)
        MODEL_CACHE[state] = model
    
    # forecast
    forecast = model.forecast(steps=steps)
    
    return {
        "state": state,
        "forecast": forecast.tolist()
    }
