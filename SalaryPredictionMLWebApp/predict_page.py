import streamlit as st
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def load_model():
    with open("saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()


regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "Sweden",
        "Spain",
        "Germany",
        "Turkey",
        "Canada",
        "France",
        "Switzerland",
        "United Kingdom of Great Britain and Northern Ireland",
        "Russian Federation",
        "Israel",
        "United States of America",
        "Brazil",
        "Italy",
        "Netherlands",
        "Poland",
        "Australia",
        "India",
        "Norway"
    )

    education = (
        'Master’s degree', 'Bachelor’s degree', 'Post grad', 'Less than a Bachelors'
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary") # True if we click on button

    if ok:
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salar is ${salary[0]:.2f}")
