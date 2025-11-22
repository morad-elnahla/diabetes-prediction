# Diabetes Prediction Project

![python](https://img.shields.io/badge/python-3.10-blue)
![streamlit](https://img.shields.io/badge/streamlit-v1.x-orange)
![status](https://img.shields.io/badge/status-experimental-yellow)

A complete machine learning project in **Python** (Jupyter Notebook) for predicting diabetes risk.  
This repo includes exploratory data analysis (EDA), visualization, model training, comparison of multiple algorithms, cross-validation, and a saved model used by a Streamlit app for inference.

---

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Notebook (analysis & training)](#notebook-analysis--training)
- [Dataset Description](#dataset-description)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Modeling](#modeling)
- [Model Evaluation](#model-evaluation)
- [Cross Validation](#cross-validation)
- [Saving the Model](#saving-the-model)
- [Streamlit App](#streamlit-app)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Files in this repo](#files-in-this-repo)
- [Next steps & suggestions](#next-steps--suggestions)
- [License](#license)

---

# 📈 Project Overview

This project performs end-to-end diabetes prediction:

- Load & inspect dataset  
- Clean and preprocess data (handle missing values / outliers)  
- Exploratory Data Analysis with visualizations (countplots, boxplots, heatmaps)  
- Feature scaling and preparation  
- Train and compare multiple ML algorithms  
- Cross-validate best models  
- Save the chosen model for deployment (`glucose_predict.sav`)  
- Use a Streamlit app (`glucose_app.py`) to serve predictions in realtime

---

## 🗒 Notebook (analysis & training)

The full interactive notebook with the analysis and model training is included locally:

**Notebook (local path):** `/mnt/data/diabets.ipynb`

> Open this Jupyter Notebook to see the exact code, outputs, plots, and model selection steps.

---

# 🗂 Dataset Description

`data.csv` (included) contains common clinical and biometric features used for diabetes prediction such as:

- `Pregnancies`  
- `Glucose`  
- `BloodPressure`  
- `SkinThickness`  
- `Insulin`  
- `BMI`  
- `DiabetesPedigreeFunction`  
- `Age`  
- `Outcome` (0 = no diabetes, 1 = diabetes)

Goal: binary classification — predict the `Outcome`.

---

# 🔍 Exploratory Data Analysis

Notebook includes:

- `df.info()` and `df.describe()`  
- Missing values check and handling  
- Duplicates check  
- Correlation matrix and heatmap  
- Distribution plots for features and target  
- Boxplots to inspect outliers  
- Pairwise relationships and feature inspection

These EDA steps help choose preprocessing and feature transformations.

---

# 🤖 Modeling

Trained and compared multiple algorithms:

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Naive Bayes  
- Decision Tree  
- Random Forest  
- AdaBoost / Gradient Boosting (if implemented)  
- Stacking / Ensemble methods

Typical pipeline used in notebook:
1. Train/test split  
2. StandardScaler (or MinMax) for feature scaling  
3. Fit each model and calculate metrics  
4. Collect metrics into a results DataFrame for comparison

![image](https://github.com/ةmorad-elnahla/app)


---

# 🧾 Model Evaluation

For each model we compute:

- Accuracy  
- Recall (sensitivity)  
- F1 score

Example result table in the notebook:

```python
final_result = pd.DataFrame({
    'Algorithm': model_names,
    'Accuracy': accuracy_list,
    'Recall Score': recall_list,
    'F1 Score': f1_list
})


