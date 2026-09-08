from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path


app = FastAPI(title="AI Disease Risk Prediction API")


# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Find model file
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "diabetes_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)


# Input data
class PatientData(BaseModel):
    pregnancies: float
    glucose: float
    bloodPressure: float
    skinThickness: float
    insulin: float
    bmi: float
    diabetesPedigreeFunction: float
    age: float


# Test API
@app.get("/")
def home():
    return {
        "message": "AI Disease Risk Prediction API is running"
    }


# Prediction API
@app.post("/predict")
def predict(data: PatientData):

    input_data = pd.DataFrame([{
        "Pregnancies": data.pregnancies,
        "Glucose": data.glucose,
        "BloodPressure": data.bloodPressure,
        "SkinThickness": data.skinThickness,
        "Insulin": data.insulin,
        "BMI": data.bmi,
        "DiabetesPedigreeFunction": data.diabetesPedigreeFunction,
        "Age": data.age
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    risk = round(probability * 100, 2)

    if prediction == 1:
        result = "Higher predicted risk"
    else:
        result = "Lower predicted risk"

    return {
        "prediction": int(prediction),
        "result": result,
        "risk_percentage": risk
    }