import joblib
import numpy as np

# Load the trained model once
model = joblib.load("model/xgb_model.pkl")

def predict_risk(features: list[float]) -> int:
    """
    Predicts risk (0 = safe, 1 = fraud) based on 29 feature values.
    """
    input_array = np.array([features])
    prediction = model.predict(input_array)
    return int(prediction[0])
