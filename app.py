import streamlit as st
import pandas as pd
import pickle

# Load your trained model
import gdown
import os
import pickle

model_path = "model.pkl"

if not os.path.exists(model_path):
    url = "https://drive.google.com/uc?id=1a2b3c4d5e6f7g8h9i"
    gdown.download(url, model_path, quiet=False)

with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Term Deposit Subscription Predictor")


# Inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ["admin.", "technician", "services", "management", "retired", "blue-collar", "unemployed", "entrepreneur", "student", "housemaid", "self-employed"])
marital = st.selectbox("Marital Status", ["married", "single", "divorced"])
education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])
balance = st.number_input("Balance", -2000, 100000, 1000)
housing = st.selectbox("Has Housing Loan?", ["yes", "no"])
loan = st.selectbox("Has Personal Loan?", ["yes", "no"])

# Preprocessing input (simplified — match your training preprocessing steps!)
input_df = pd.DataFrame({
    'age': [age],
    'job_' + job: [1],
    'marital_' + marital: [1],
    'education_' + education: [1],
    'balance': [balance],
    'housing_yes': [1 if housing == "yes" else 0],
    'loan_yes': [1 if loan == "yes" else 0]
})

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Prediction: {'Subscribed' if prediction == 1 else 'Not Subscribed'}")
