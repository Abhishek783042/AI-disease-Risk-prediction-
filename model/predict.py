import joblib
import numpy as np


# Load trained model
model = joblib.load("diabetes_model.pkl")

print("AI Disease Risk Prediction")
print("--------------------------")

# Take input
pregnancies = float(input("Enter Pregnancies: "))
glucose = float(input("Enter Glucose: "))
blood_pressure = float(input("Enter Blood Pressure: "))
skin_thickness = float(input("Enter Skin Thickness: "))
insulin = float(input("Enter Insulin: "))
bmi = float(input("Enter BMI: "))
diabetes_pedigree = float(input("Enter Diabetes Pedigree Function: "))
age = float(input("Enter Age: "))


# Create input
data = np.array([[
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree,
    age
]])


# Prediction
prediction = model.predict(data)[0]

# Probability
probability = model.predict_proba(data)[0][1]

risk = round(probability * 100, 2)


# Display result
print("\n--------------------------")

if prediction == 1:
    print("Result: Higher predicted risk")
else:
    print("Result: Lower predicted risk")

print("Risk Score:", risk, "%")

print("--------------------------")
print("Educational prediction only.")