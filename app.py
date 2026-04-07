import streamlit as st
import numpy as np
import joblib

model = joblib.load('model.pkl')

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Prediction App")
st.write("Fill in the details below to estimate house price.")

st.sidebar.header("🏡 House Features")

# Better inputs with explanations

CRIM = st.sidebar.slider(
    "Crime Rate in Area",
    0.0, 10.0, 0.1,
    help="Higher value means more crime in the area"
)

ZN = st.sidebar.slider(
    "Residential Land Percentage",
    0.0, 100.0, 0.0,
    help="Percentage of residential land zoned for large lots"
)

INDUS = st.sidebar.slider(
    "Non-Retail Business Area",
    0.0, 30.0, 10.0,
    help="Proportion of non-retail business area"
)

CHAS = st.sidebar.selectbox(
    "Near River?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

NOX = st.sidebar.slider(
    "Air Pollution (NOX level)",
    0.3, 1.0, 0.5,
    help="Higher means more pollution"
)

RM = st.sidebar.slider(
    "Average Number of Rooms",
    3.0, 9.0, 6.0,
    help="More rooms generally increase price"
)

AGE = st.sidebar.slider(
    "Age of Property (%)",
    0.0, 100.0, 50.0,
    help="Percentage of old buildings"
)

DIS = st.sidebar.slider(
    "Distance to Employment Centers",
    1.0, 10.0, 4.0,
    help="Higher means farther away"
)

RAD = st.sidebar.slider(
    "Highway Accessibility",
    1.0, 25.0, 5.0,
    help="Ease of access to highways"
)

TAX = st.sidebar.slider(
    "Property Tax Rate",
    100.0, 800.0, 300.0,
    help="Higher tax may reduce value"
)

PTRATIO = st.sidebar.slider(
    "Student-Teacher Ratio",
    10.0, 25.0, 15.0,
    help="Higher ratio = worse schools"
)

B = st.sidebar.slider(
    "Diversity Index (B)",
    0.0, 400.0, 350.0
)

LSTAT = st.sidebar.slider(
    "Lower Income Population (%)",
    1.0, 40.0, 10.0,
    help="Higher value usually lowers price"
)

# Prediction
if st.button("Predict Price"):

    # transformations
    CRIM = np.log1p(CRIM)
    ZN = np.log1p(ZN)
    DIS = np.log1p(DIS)
    RAD = np.log1p(RAD)
    LSTAT = np.log1p(LSTAT)

    input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE,
                            DIS, RAD, TAX, PTRATIO, B, LSTAT]])

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated House Price: ${prediction[0]*1000:.2f}")