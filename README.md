# Car Price Prediction (XGBoost + Flask + Streamlit)

This project is an end-to-end Machine Learning application that predicts used car prices based on features like manufacturing year, kilometers driven, fuel type, transmission type, and ownership details.  
It combines a trained XGBoost model, a Flask backend API, and a Streamlit-based user interface.

---

## Features
- Machine Learning model built using **XGBoost Regressor**
- Complete **data cleaning and feature engineering**
- **Flask API backend** to serve predictions
- **Streamlit UI** for user-friendly inputs and real-time results
- End-to-end workflow: Notebook → Model Training → API → UI

---

## Tech Stack
**Languages:** Python  
**Libraries:** XGBoost, Pandas, NumPy, Scikit-Learn  
**Frameworks:** Flask, Streamlit  
**Tools:** Jupyter Notebook, Git/GitHub

---

## Project Structure
car_price_prediction/
```
│── app.py # Flask backend API
│── streamlit_app.py # Streamlit interface
│── CarPricePrediction.ipynb # EDA + model training notebook
│── model.pkl / model.json # Trained model
│── requirements.txt # Dependencies
│── README.md # Documentation
```


## How to Run

### 1. Clone the Repository
```
git clone https://github.com/Vxrun10/car_price_prediction.git

cd car_price_prediction
```


### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the Flask API
```
python app.py
```


### 4. Run the Streamlit App
```
streamlit run streamlit_app.py
```


---

## Usage
1. Open the Streamlit interface in your browser  
2. Enter car details  
3. Click **Predict**  
4. The app will display the estimated car price

---


## Contact
**Varun Panchal**  
(Varunpanchal1008@gmail.com)
