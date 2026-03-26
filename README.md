# **Flight Delay Prediction System**

##  **Overview**
This project predicts whether a flight will be delayed or on time using Machine Learning. It also provides an interactive dashboard for user input and data visualization.

---

## **Features**
- Predict flight delay (On-time / Delayed)
- Random Forest Machine Learning model
- Feature engineering and data preprocessing
- Interactive Streamlit dashboard
- Visual insights (feature importance, delay distribution)

--

## **Tech Stack**
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib, Seaborn
- Joblib

---

##  **How it Works**
1. User enters flight details (month, airline, airport, delay, etc.)
2. Model processes input features
3. Prediction is generated (Delayed or On-Time)
4. Dashboard displays insights and graphs

---

## 📷 Dashboard Preview
<img width="1897" height="921" alt="image" src="https://github.com/user-attachments/assets/b5c17e31-c9df-4caa-8df3-18d735c89d14" />


---

## **Key Insight**
Departure delay is the most important factor affecting arrival delays.

---

##  **Note**
- Dataset is not included due to size limitations
- Model file may not be included if exceeding GitHub limits

---

## **For Running Locally**

```bash
pip install -r requirements.txt
streamlit run app.py
