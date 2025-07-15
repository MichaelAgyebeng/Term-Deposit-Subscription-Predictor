import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("random_forest_model.pkl")

# UI
st.title("Subscription Predictor")

# User input
st.header("Client Info")
age = st.number_input("Age", 18, 100, 35)
job = st.selectbox("Job", ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired',
                           'self-employed', 'services', 'student', 'technician', 'unemployed'])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has Default?", ['yes', 'no'])
housing = st.selectbox("Has Housing Loan?", ['yes', 'no'])
loan = st.selectbox("Has Personal Loan?", ['yes', 'no'])
duration = st.number_input("Call Duration (seconds)", 0, 10000, 100)
campaign = st.number_input("Campaign Contacts", 1, 50, 1)
pdays = st.number_input("Days Since Last Contact", -1, 999, -1)
previous = st.number_input("Previous Contacts", 0, 100, 0)
poutcome = st.selectbox("Previous Outcome", ['failure', 'success', 'nonexistent', 'unknown'])

if st.button("Predict"):
    input_df = pd.DataFrame([{
        'age': age,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'job_' + job: 1,
        'marital_' + marital: 1,
        'education_' + education: 1,
        'default_yes': 1 if default == 'yes' else 0,
        'housing_yes': 1 if housing == 'yes' else 0,
        'loan_yes': 1 if loan == 'yes' else 0,
        'poutcome_' + poutcome: 1,
    }])

    # Fill missing dummies
    all_features = model.feature_names_in_
    for col in all_features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[all_features]

    pred = model.predict(input_df)[0]
    st.success(f"Prediction: {'Subscribed' if pred == 1 else 'Not Subscribed'}")
