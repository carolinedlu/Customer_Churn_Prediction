import streamlit as st
import pandas as pd
from src.pipelines.predict_pipeline import ModelPrediction

data = pd.DataFrame({
    'Age': [10],  # Use a list with a single value
    'Gender': ['Male'],  # Use a list with a single value
    'Location': ['Los Angeles'],  # Use a list with a single value
    'Subscription_Length_Months': [5],  # Use a list with a single value
    'Monthly_Bill': [100],  # Use a list with a single value
    'Total_Usage_GB': [100]  # Use a list with a single value
})

# Calling prediction pipeline to predict the output


predictor = ModelPrediction()
x = predictor.prediction(data)

print(x)









