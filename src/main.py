from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Customer Segmentation API")

# Load model safely
MODEL_PATH = os.path.join(os.path.dirname(__file__), "segmentation_model.pkl")
model = joblib.load(MODEL_PATH)


class CustomerInput(BaseModel):
    recency: float
    frequency: float
    monetary: float


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_segment(data: CustomerInput):
    cluster = model.predict([[data.recency, data.frequency, data.monetary]])
    return {"segment": int(cluster[0])}
