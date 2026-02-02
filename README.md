# bank-loan-application-ml

Project Overview

The Bank Loan Application System is an end-to-end machine learning application that predicts the probability of loan default and makes real-time loan approval decisions using a recall-optimized Decision Tree model.

The system follows real banking workflows, separating KYC data from risk-assessment features, applying business-defined credit policies, and deploying the final solution as a production-ready web application using Streamlit.

🏗 Project Architecture

User Input (Web Application)                                                                                                                                                  
                ↓                                                                                                                                                             
KYC Validation (Compliance Only – Not Used in ML)                                                                                                                             
                ↓                                                                                                                                                             
Credit Score → Loan Grade Mapping (Bank Policy Rules)                                                                                                                         
                ↓                                                                                                                                                             
Feature Engineering & Encoding                                                                                                                                                
                ↓                                                                                                                                                             
Decision Tree Model (Trained ML Model)                                                                                                                                        
                ↓                                                                                                                                                             
Default Probability Prediction                                                                                                                                                
                ↓                                                                                                                                                             
Business Threshold Evaluation (0.4)                                                                                                                                           
                ↓                                                                                                                                                             
Final Loan Approval / Rejection                                                                                                                                                     



