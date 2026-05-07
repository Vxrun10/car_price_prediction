import numpy as np
import datetime
import xgboost as xgb
import streamlit as st
import pandas as pd

def main():
    html_temp = "<h1>Car Price Prediction</h1>"

    model = xgb.Booster()
    model.load_model("xgb_model.json")

    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This app will help you to predict your car selling price")

    p1 = st.number_input("Ex-showroom price (Lakh)", 2.5, 25.0, step=1.0)
    p2 = st.number_input("Kms driven", 100, 500000, step=100)

    s1 = st.selectbox("Fuel type", ("Petrol", "Diesel", "CNG"))
    p3 = {"Petrol": 0, "Diesel": 1, "CNG": 2}[s1]

    s2 = st.selectbox("Seller type", ("Dealer", "Individual"))
    p4 = {"Dealer": 0, "Individual": 1}[s2]

    s3 = st.selectbox("Transmission", ("Manual", "Automatic"))
    p5 = {"Manual": 0, "Automatic": 1}[s3]

    p6 = st.slider("Number of owners", 0, 5)

    current_year = datetime.datetime.now().year
    years = st.number_input("Car purchased year", 1990, current_year, step=1)
    p7 = current_year - years
    

    # Convert to numpy array
    data = np.array([[p1, p2, p3, p4, p5, p6, p7]])
    
    # Create dataframe with feature names
    data = pd.DataFrame([{
    'Present_Price': p1,
    'Kms_Driven': p2,
    'Fuel_Type': p3,
    'Seller_Type': p4,
    'Transmission': p5,
    'Owner': p6,
    'Age': p7
    }])


    # Convert to DMatrix
    dmatrix = xgb.DMatrix(data)

    if st.button("Predict"):
        pred = model.predict(dmatrix)
        st.success(f"You can sell your car at {pred[0]:.2f} lakhs")

if __name__ == '__main__':
    main()