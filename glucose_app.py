import pickle
import streamlit as st
import pandas as pd

loaded = pickle.load(open('glucose_predict.sav', 'rb'))
model = loaded['model']
scaler = loaded['scaler']
selector = loaded['selector']

# عنوان وشرح
st.title('Diabetes Prediction Web App')
st.info('Easy Application For Diabetes Prediction Disease')

# مدخلات من الـ sidebar زي ما انت عامل
st.sidebar.header('Feature Selection')

Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
Insulin = st.text_input('Insulin')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')

# الزرار في الـ sidebar زي كودك
button = st.sidebar.button('confirm')

if button:
    try:
        # الداتا زي ما هي لكن أرقام
        df = pd.DataFrame({
            'Pregnancies': [int(Pregnancies)],
            'Glucose': [float(Glucose)],
            'BloodPressure': [float(BloodPressure)],
            'SkinThickness': [float(SkinThickness)],
            'Insulin': [float(Insulin)],
            'BMI': [float(BMI)],
            'DiabetesPedigreeFunction': [float(DiabetesPedigreeFunction)],
            'Age': [int(Age)]
        })

        # نفس خطوات التدريب: feature selection + scaling
        selected = selector.transform(df)
        scaled = scaler.transform(selected)

        result = model.predict(scaled)


        if result[0] == 1:
            st.error("⚠️ The person is likely to have diabetes.")
            st.image('bad.jpg',width=600)
        else:
            st.success("✅ The person is unlikely to have diabetes.")
            st.image('good.jpg',width=600)

    except Exception as e:
        st.warning(f"❗ Please enter all inputs correctly. Error: {e}")
