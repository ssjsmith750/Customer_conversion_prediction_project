import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
import datetime

# Load saved model from file
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Insurance Prediction App", page_icon=":money_with_wings:")

st.write("# Insurance Subscription Prediction App")

# Background Image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2016/09/13/19/31/texture-1668079_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# Create input fields for user input
age_options = ["Please select"] + [i for i in range(18, 101)]
age = st.selectbox("Age", age_options)

job_options = ["Please select", "admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"]
job = st.selectbox("Job", job_options)

marital_options = ["Please select", "divorced", "married", "single"]
marital = st.selectbox("Marital Status", marital_options)

education_options = ["Please select", "primary", "secondary", "tertiary", "unknown"]
education = st.selectbox("Education", education_options)

call_type_options = ["Please select", "cellular", "telephone", "unknown"]
call_type = st.selectbox("Call Type", call_type_options)

day_options = ["Please select"] + [i for i in range(1, 32)]
day = st.selectbox("Day of Month", day_options)

month_options = ["Please select"] + [i for i in range(1, 13)]
month = st.selectbox("Month", month_options)

duration_options = ["Please select"] + [i for i in range(5001)]
duration = st.selectbox("Last Contact Duration", duration_options)

num_calls_options = ["Please select"] + [i for i in range(1001)]
num_calls = st.selectbox("No of calls ", num_calls_options)

previous_options = ["Please select"] + [i for i in range(101)]
previous = st.selectbox("Number of Contacts Before Campaign", previous_options)


# Create user input DataFrame
user_input = pd.DataFrame({
    "age": [age],
    "job": [job],
    "marital": [marital],
    "education": [education],
    "call_type": [call_type],
    "day": [day],
    "month": [month],
    "duration": [duration],
    "num_calls": [num_calls],
    "previous": [previous]
})

# Check if any of the input fields are not filled in
if "Please select" in user_input.values:
    st.write("### Please fill in all the fields.")
else:
    # One-hot encode categorical features
    categorical_columns = ["job", "marital", "education", "call_type", "day", "month"]
    user_input_encoded = pd.get_dummies(user_input, columns=categorical_columns)
    user_input_encoded = user_input_encoded.astype('float')

    # Make prediction with XGBoost model
    prediction = model.predict(user_input_encoded)[0]

    # Display prediction to user
    if st.button("Predict"):
        if prediction == 0:
            st.write("### The customer will subscribe for insurance.")
            if prediction == 1:
                st.write("### The customer will not subscribe for insurance.")
        else:
            st.write("### The customer will not subscribe for insurance.")

