🌐 Live Demo
👉 Click here to view the app [https://term-deposit-subscription-predictor-bd5s3zcrsapvnvjkgr7bpe.streamlit.app/]

# 🏦 Term Deposit Subscription Prediction Model

This project is a machine learning solution that predicts whether a client will subscribe to a term deposit based on their demographic and interaction data. It is designed to support marketing decision-making in financial institutions.

## 📊 Problem Statement

The goal is to predict the binary target variable `y`, which indicates whether a client will subscribe to a term deposit (`yes`) or not (`no`), using a set of input features such as age, job type, marital status, balance, previous campaign outcomes, etc.

## 🚀 Features

- Cleaned and preprocessed real-world banking dataset
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Predictive modeling using:
  - Logistic Regression
  - Random Forest
- Class imbalance handling via `class_weight='balanced'`
- Model evaluation with accuracy, precision, recall, F1-score, and AUC
- Deployed via Streamlit / Hugging Face Spaces with public access

## 🛠 Tech Stack

- Python 🐍
- Pandas, Scikit-learn, Seaborn, Matplotlib
- Streamlit (for web UI)
- Hugging Face / Google Drive (for large model hosting)
- Git & GitHub

## 🧠 Model Training

The training script includes:

- Encoding categorical variables
- Handling missing and unknown values
- Creating a binary feature for `previous contact`
- Removing the `duration` column to prevent data leakage
- Splitting the dataset with `stratify=y`

## ⚖️ Evaluation Metrics

| Metric       | Description                                   |
|--------------|-----------------------------------------------|
| Accuracy     | Overall correctness of the model              |
| Precision    | True positives out of predicted positives     |
| Recall       | True positives out of actual positives        |
| F1 Score     | Harmonic mean of precision and recall         |
| ROC AUC      | Area under the ROC Curve                      |


