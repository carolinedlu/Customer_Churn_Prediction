import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import joblib
import os
# from sklearn.externals import joblib
import pickle

# Load the trained model
# model = joblib.load('your_trained_model.pkl')  # Replace 'your_trained_model.pkl' with your model file path

# Load the label and one-hot encoders
# label_encoder = joblib.load('label_encoder.pkl')  # Replace 'label_encoder.pkl' with your encoder file path
# one_hot_encoder = joblib.load('one_hot_encoder.pkl')  # Replace 'one_hot_encoder.pkl' with your encoder file path


# Streamlit UI
st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="https://drive.google.com/uc?id=1yo7ZhWaOWnmXB1JtVD9Huj0t0VmqxsIx",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS to adjust the styling
st.markdown(
    """
    <style>
    
    .stApp {
        background-color: #2d2739; /* Set your desired background color */
        padding: 20px;
        border-radius: 10px;
    }
    .stMarkdownTitle {
        font-size: 40px;
        text-align: center;

    }
    
    .stHeader {
        text-align: left;
        font-size: 24px;
    }
    .css-1avcm0n {
        background: #040406;  /* Change the navbar color to your desired color */
    }
    .st-br {
    color: #040406;
    border: none;
    background-color: #695b85
    }
    
    
    .st-bw {
    background-color: #695b85;
    border: none;
    color: #040406
    }
    .st-di  {
    background-color: #695b85;
    border: none;
    color: #040406
    }
    .css-1hgxyac  {
    background-color: #695b85;
    border: none;
    color: #040406

    }
    
    .css-1hgxyac.focused  {
    background-color: #695b85;
    border: none;
    color: #040406

    }
    
    .css-1hdbmx1.focused {
       border: none;
    }

    .custom-button {
        background-color: #695b85;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s; /* Add a smooth transition for background color change */
    }

    .custom-button:active {
        background-color: green; /* Change the background color when the button is clicked (active) */
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI with centered title and left-aligned header
st.markdown("<h1 class='stMarkdownTitle'>CUSTOMER CHURN PREDICTION APP</h1>", unsafe_allow_html=True)
st.header('Input Customer Information')

# Set the page layout to centered and limit width
st.markdown(
    """
    <style>
    .stApp {
        max-width: 10000px; /* Adjust the content width as needed */
        margin: 0 auto;
        padding: 0rem 1rem 10rem; /* Add padding to the bottom for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI elements
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=0)
location = st.selectbox('Location', ['Los Angeles', 'New York', 'Miami', 'Houston', 'Chicago'])
subscription_length = st.number_input('Subscription Length (Months)', min_value=0)
monthly_bill = st.number_input('Monthly Bill', min_value=0.0)
total_usage_gb = st.number_input('Total Usage GB', min_value=0.0)



# if st.button('Predict Churn'):
#     # Prepare the data for the model
#     data = pd.DataFrame({
#         'Age': [age],
#         'Subscription Length (Months)': [subscription_length],
#         'Monthly Bill': [monthly_bill],
#         'Total Usage GB': [total_usage_gb],
#         # 'Gender': label_encoder.transform([gender]),
#         # 'Location': one_hot_encoder.transform([[location]])
#         'Gender': [gender],
#         'Location': [location]
#     })










# Load the transformer.pkl file (you need to provide the correct file path)

transformer_path = os.path.join('artifacts', 'transformer.pkl')
transformation_pipeline = joblib.load( transformer_path)

# Load the model.pkl file (you need to provide the correct file path)
model_path = os.path.join( 'artifacts', 'model.pkl')
model = joblib.load(model_path)


if st.button('Predict Churn'):
    # Prepare the data for the model
    data = pd.DataFrame({
        'Age': [age],
        'Subscription Length (Months)': [subscription_length],
        'Monthly Bill': [monthly_bill],
        'Total Usage GB': [total_usage_gb],
        'Gender': [gender],
        'Location': [location]
    })

    # Transform the user input data using the transformation pipeline
    transformed_data = transformation_pipeline.transform(data)

    # Make the prediction using the model
    prediction = model.predict(transformed_data)
    
    # Return the prediction
    st.subheader('Churn Prediction:')
    if prediction == 0:
        st.write('The customer is likely to stay (Churn: No)')
    else:
        st.write('The customer is likely to churn (Churn: Yes)')
        
        
        
        
        
        
        
        
        
        
        
    # Make the prediction
    prediction = model.predict(data)
    # Return the prediction
    st.subheader('Churn Prediction:')
    if prediction == 0:
        st.write('The customer is likely to stay (Churn: No)')
    else:
        st.write('The customer is likely to churn (Churn: Yes)')



#    python app.py

#    streamlit run app.py
