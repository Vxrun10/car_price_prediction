import pandas as pd
import numpy as np
import datetime
import xgboost as Xgb
import streamlit as st

def main():
    html_temp = """
      <h1> Car Price Prediction</h1>
    """
    model =Xgb.XGBRegressor()
    model.load_model("xgb_model.json")
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.markdown("This app will help you to predict your car selling price")
    p1 =st.number_input("Please enter ex-showroom price (In Lakh)",2.5,25.0,step=1.0)
    p2 =st.number_input("Please enter car drive (In kilometer)",100,500000,step=100)
    s1 =st.selectbox("Select the fuel_type",("Petrol","Diesel","CNG"))
    
    
    if s1=='Petrol':
        p3=0
    elif s1 =='Diesel':
        p3=1
    elif s1=='CNG':
        p3=2
    
    
    s2 =st.selectbox("Select the seller type",("Dealer","Individual"))  
    
    
    if s2=='Dealer':
        p4=0
    elif s2=='Individual':  
        p4=1    
        
    s3 = st.selectbox("Select the transmission",("Maunal","Autommatic"))
    
    if s3=='Maunal':
        p5=0
    elif s3=='Autommatic':
        p5=1    
        
    p6 =st.slider("How many owners",0,5)
    
    data_time=datetime.datetime.now() 
    
    years= st.number_input("Car purchesd year",1990,data_time.year,step=1)
    
    p7 =data_time.year -years
    
    data_new =pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
    },index=[0])   
    
    if st.button("predict"):
        pred= model.predict(data_new)
        st.success("you can sell your car at{:.2f} lakhs".format(pred[0]))



if __name__=='__main__':
    main()