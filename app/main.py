# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_risk

app = FastAPI()

# Health check route
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Request schema
class PredictionRequest(BaseModel):
    features: list[float]

# Predict route
@app.post("/predict")
def predict(request: PredictionRequest):
    if len(request.features) != 30:
        raise HTTPException(status_code=400, detail="Input must contain exactly 30 features")
    prediction = predict_risk(request.features)
    label = "RISKY" if prediction == 1 else "SAFE"
    return {"prediction": prediction, "label": label}
