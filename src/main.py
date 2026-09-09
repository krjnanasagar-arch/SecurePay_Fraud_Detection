from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="SecurePay Fraud Detection API",
    description="API for detecting fraudulent credit card transactions",
    version="1.0"
)

# --------------------------------------------------
# Load trained model and scaler
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "isolation_forest_model.pkl"
)

SCALER_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "robust_scaler.pkl"
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("Model and scaler loaded successfully!")


# --------------------------------------------------
# Input data structure
# --------------------------------------------------

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model": "Isolation Forest",
        "contamination": 0.005
    }


# --------------------------------------------------
# Fraud prediction
# --------------------------------------------------

@app.post("/predict")
def predict(transaction: Transaction):

    data = transaction.model_dump()

    df = pd.DataFrame([data])

    # Scale Amount exactly as done during training
    df["Amount"] = scaler.transform(df[["Amount"]])

    # Make prediction
    prediction = model.predict(df)[0]

    # Isolation Forest:
    # -1 = anomaly
    #  1 = normal

    if prediction == -1:
        result = "Fraud"
    else:
        result = "Normal"

    return {
        "prediction": result,
        "model": "Isolation Forest"
    }