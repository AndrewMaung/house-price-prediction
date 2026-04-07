# 🏠 House Price Prediction App

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts house prices based on various features such as crime rate, number of rooms, pollution level, and more.

The model is trained using a **Random Forest Regressor**, achieving strong predictive performance, and is deployed as an interactive web application using Streamlit.

---

## 🚀 Live Demo

https://house-price-prediction-amo24.streamlit.app/

---

## 🎯 Features

* 📊 Data preprocessing (handling skewness with log transformation)
* 🤖 Machine Learning model using Random Forest
* 🎛️ User-friendly interface with sliders and dropdowns
* ⚡ Real-time predictions
* 📈 Model evaluation using R² score and MSE

---

## 🧠 Model Details

* **Algorithm:** Random Forest Regressor
* **R² Score:** ~0.89
* **Mean Squared Error:** ~7.9

The model captures complex, non-linear relationships between housing features and price, outperforming basic linear regression.

---

## 📊 Input Features Explained

| Feature | Description                          |
| ------- | ------------------------------------ |
| CRIM    | Crime rate in the area               |
| ZN      | Residential land percentage          |
| INDUS   | Non-retail business area             |
| CHAS    | Proximity to river (0 = No, 1 = Yes) |
| NOX     | Air pollution level                  |
| RM      | Average number of rooms              |
| AGE     | Age of property                      |
| DIS     | Distance to employment centers       |
| RAD     | Highway accessibility                |
| TAX     | Property tax rate                    |
| PTRATIO | Student-teacher ratio                |
| B       | Diversity index                      |
| LSTAT   | % of lower-income population         |

---

## ⚙️ Tech Stack

* **Python**
* **Scikit-learn**
* **Streamlit**
* **NumPy**
* **Pandas**
* **Joblib**

---

## 📁 Project Structure

```
House Price Prediction/
│
├── app.py              # Streamlit app
├── model.pkl           # Trained ML model
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone YOUR_REPO_LINK
cd house-price-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🔧 Preprocessing

Some features are transformed using **log transformation** to reduce skewness and improve model performance:

* CRIM
* ZN
* DIS
* RAD
* LSTAT

This ensures better learning and more stable predictions.

---

## 📈 Model Evaluation

The model was evaluated using:

* **R² Score** → Measures how well the model explains variance
* **MSE (Mean Squared Error)** → Measures prediction error

Residual analysis was also performed to ensure:

* No major patterns in errors
* Good generalization

---

## 🚀 Future Improvements

* Add SHAP values for model explainability
* Try advanced models like XGBoost
* Improve UI with charts and insights
* Add input validation and recommendations

---

## 💡 Key Learnings

* Importance of data preprocessing
* Handling skewed data
* Difference between linear and non-linear models
* Model evaluation techniques
* Building and deploying ML apps

---

## 📬 Contact

Feel free to connect or reach out for feedback!

---

⭐ If you like this project, consider giving it a star on GitHub!
