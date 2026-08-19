import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load('logisitic_model.pkl')

st.title('Loan Prediction App')
st.write('Enter the input values:')

#input fields
loan_amnt = st.number_input('Loan amount:',value = 10000)
loan_int_rate = st.number_input('Loan interest:',value = 12.0)
person_income = st.number_input('Person Income:',value = 100000)
loan_percent_income = st.number_input('Loan percent in Income',min_value = 0.0,max_value =100.0,step = 100.0)
person_home_ownership_RENT = 1 if st.selectbox("House Type(Own/Rent)",['Own house','Rented']) == 'Own house' else 0
loan_intent_EDUCATION = 1 if st.selectbox('Loan purpose(Education)',['Yes','No']) == 'Yes' else 0
loan_intent_VENTURE = 1 if st.selectbox('Loan purpose(House purpose)',['Yes','No']) == 'Yes' else 0
person_gender_male = 1 if st.selectbox('Gender',['Male','Female']) == 'Male' else 0
previous_loan_defaults_on_file_Yes = 1 if st.selectbox('Any previeous loan defaults',['Yes','No']) == 'Yes' else 0

collect_input = np.array([[loan_int_rate, previous_loan_defaults_on_file_Yes,
       loan_percent_income, person_income, loan_amnt,
       person_home_ownership_RENT, loan_intent_EDUCATION,
       loan_intent_VENTURE, person_gender_male]])

if st.button("Predict"):
    prediction = model.predict(collect_input)
    if prediction ==1:
        st.success('loan approved')
    else:
        st.error('loan not approved')

    