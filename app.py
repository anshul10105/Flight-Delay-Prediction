import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load("flight_model.pkl")

# Load dataset (for real graphs)
df = pd.DataFrame({
    "ARRIVAL_DELAY": np.random.normal(10, 30, 1000)
})
# Page config
st.set_page_config(page_title="Flight Delay Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>✈️ Flight Delay Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>ML-based delay prediction system with insights</h4>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("🧾 Flight Inputs")

month = st.sidebar.selectbox("Month", list(range(1, 13)))
day = st.sidebar.selectbox("Day", list(range(1, 32)))
day_of_week = st.sidebar.selectbox("Day of Week", list(range(1, 8)))

# Airline mapping
airline_mapping = {
    "AA": 0,
    "DL": 1,
    "UA": 2,
    "WN": 3
}
airline = st.sidebar.selectbox("Airline", list(airline_mapping.keys()))
airline_encoded = airline_mapping[airline]

# Airport mapping (example)
airport_mapping = {
    "ATL": 0,
    "LAX": 1,
    "ORD": 2,
    "DFW": 3,
    "DEN": 4
}

origin_airport = st.sidebar.selectbox("Origin Airport", list(airport_mapping.keys()))
destination_airport = st.sidebar.selectbox("Destination Airport", list(airport_mapping.keys()))

origin = airport_mapping[origin_airport]
destination = airport_mapping[destination_airport]

departure_delay = st.sidebar.slider("Departure Delay", -50, 500, 0)
distance = st.sidebar.slider("Distance", 0, 5000, 500)

# Feature engineering
is_weekend = 1 if day_of_week >= 6 else 0

# Prediction
if st.sidebar.button("🚀 Predict"):

    input_data = np.array([[month, day, day_of_week,
                            airline_encoded, origin, destination,
                            departure_delay, distance, is_weekend]])

    prediction = model.predict(input_data)

    st.markdown("## 🎯 Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Flight will be DELAYED")
    else:
        st.success("✅ Flight will be ON TIME")

    st.info("💡 Tip: Higher departure delay increases chance of arrival delay.")

# ========================
# 📊 INSIGHTS SECTION
# ========================

st.markdown("---")
st.header("📊 Insights Dashboard")

# Feature Importance (REAL)
features = ["Month", "Day", "Day of Week", "Airline", "Origin", "Destination", "Departure Delay", "Distance", "Weekend"]
importances = model.feature_importances_

fig, ax = plt.subplots()
ax.barh(features, importances)
ax.set_title("Feature Importance")
st.pyplot(fig)

# Real Delay Distribution
fig2, ax2 = plt.subplots()
sns.histplot(df['ARRIVAL_DELAY'].clip(-50, 200), bins=30, ax=ax2)
ax2.set_title("Real Delay Distribution")
st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built by Anshul Singh 🚀</p>", unsafe_allow_html=True)