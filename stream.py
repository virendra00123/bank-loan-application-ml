import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import uuid

# =========================================================
# Page Config
# =========================================================
st.set_page_config(
    page_title="Bank Loan Application System",
    page_icon="🏦",
    layout="centered"
)



# =========================================================
# Load Model
# =========================================================
import joblib

bundle = joblib.load("credit_risk_model.joblib")

model = bundle["model"]
threshold = bundle["threshold"]


# =========================================================
# Encoding Functions (MUST MATCH TRAINING)
# =========================================================
def credit_score_to_grade(score):
    if score >= 700:
        return 1  # A
    elif score >= 650:
        return 2  # B
    elif score >= 600:
        return 3  # C
    elif score >= 550:
        return 4  # D
    elif score >= 500:
        return 5  # E
    elif score >= 450:
        return 6  # F
    else:
        return 7  # G

def loan_intent_num(intent):
    mapping = {
        "PERSONAL": 1,
        "EDUCATION": 2,
        "MEDICAL": 3,
        "VENTURE": 4,
        "HOMEIMPROVEMENT": 5,
        "DEBTCONSOLIDATION": 6
    }
    return mapping[intent]

def default_record(val):
    return 0 if val == "N" else 1

def ownership(home):
    mapping = {
        "OWN": 1,
        "MORTGAGE": 2,
        "RENT": 3,
        "OTHERS": 0
    }
    return mapping[home]

# =========================================================
# Header
# =========================================================
st.markdown(
    "<h1 style='text-align:center;'>🏦 Bank Loan Application System</h1><hr>",
    unsafe_allow_html=True
)

# =========================================================
# KYC (NOT USED IN MODEL)
# =========================================================
st.subheader(" Applicant Identity (KYC)")

c1, c2 = st.columns(2)
with c1:
    full_name = st.text_input("Full Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
with c2:
    profession = st.text_input("Profession")
    contact_number = st.text_input("Contact Number")

# =========================================================
# Risk Inputs
# =========================================================
st.subheader(" Credit Risk Assessment")

c3, c4 = st.columns(2)
with c3:
    person_age = st.number_input("Age", 18, 100, 30)
    person_income = st.number_input("Annual Income (₹)", 1000, value=50000)
    person_home_ownership = st.selectbox(
        "Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHERS"]
    )
    person_emp_length = st.number_input("Employment Length (Years)", 0.0, 60.0, 5.0)

with c4:
    loan_intent = st.selectbox(
        "Loan Purpose",
        ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE",
         "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    )
    loan_amnt = st.number_input("Loan Amount (₹)", 500, value=10000)
    loan_int_rate = st.number_input("Interest Rate (%)", 0.0, 40.0, 15.0)

# =========================================================
# Credit Info
# =========================================================
st.subheader(" Credit Information")

credit_score = st.number_input("Credit Score", 300, 900, 700)
loan_grade = credit_score_to_grade(credit_score)

grade_map = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
st.info(f"Loan Grade: **{grade_map[loan_grade]}**")

cb_person_default_on_file = default_record(
    st.selectbox("Previous Default?", ["N", "Y"])
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length (Years)", 0, 50, 5
)

loan_percent_income = loan_amnt / person_income

# =========================================================
# Submit
# =========================================================
if st.button(" Submit Loan Application"):
    app_id = str(uuid.uuid4())[:8].upper()

    input_df = pd.DataFrame([{
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": ownership(person_home_ownership),
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent_num(loan_intent),
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }])

    prob = model.predict_proba(input_df)[:, 1][0]
    decision = "REJECTED " if prob >= threshold else "APPROVED "

    st.subheader("Loan Decision")
    st.write(f"Application ID: `{app_id}`")
    st.write(f"Applicant: **{full_name}**")
    # st.write(f"Default Probability: **{prob:.2%}**")
    st.write(f"Decision: **{decision}**")

# =========================================================
# Footer
# =========================================================
st.markdown(
    "<hr><p style='text-align:center;font-size:12px;'>© 2026 Bank Loan Application</p>",
    unsafe_allow_html=True
)
