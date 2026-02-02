# bank-loan-application-ml

Project Overview

The Bank Loan Application System is an end-to-end machine learning application that predicts the probability of loan default and makes real-time loan approval decisions using a recall-optimized Decision Tree model.

The system follows real banking workflows, separating KYC data from risk-assessment features, applying business-defined credit policies, and deploying the final solution as a production-ready web application using Streamlit.

Project Architecture:

User Input (Web App)                                                                                                                                                          
        ↓
KYC Validation (Not used in ML)                                                                                                                                               
        ↓
Credit Score → Loan Grade Mapping                                                                                                                                             
        ↓
ML Feature Processing
        ↓
Decision Tree Model
        ↓
Probability of Default
        ↓
Threshold (0.4)                                                                                                                                                               
        ↓
Loan Approval / Rejection                                                                                                                                                      



