import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_model(state):
    model_path = os.path.join(BASE_DIR, "models", f"{state}_sarima.pkl")
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    
    return model
