from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_risk
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(request: PredictionRequest):
    if len(request.features) != 30:
        raise HTTPException(status_code=400, detail="Input must contain exactly 30 features")
    prediction = predict_risk(request.features)
    label = "RISKY" if prediction == 1 else "SAFE"
    return {"prediction": prediction, "label": label}
