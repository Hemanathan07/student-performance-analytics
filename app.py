import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("🎓 Student Placement Predictor")
st.write("Enter a student's details to predict placement likelihood.")

model = pickle.load(open("models/placement_pipeline.pkl", "rb"))

attendance = st.slider("Attendance (%)", 0, 100, 80)
study_hours = st.slider("Study Hours per day", 0, 12, 5)
average_mark = st.slider("Average Mark", 0, 100, 70)

study_attendance_score = study_hours * attendance / 100

if st.button("Predict Placement"):
    features = pd.DataFrame(
        [[attendance, study_hours, average_mark, study_attendance_score]],
        columns=["attendance", "study_hours", "average_mark", "study_attendance_score"]
    )
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ LIKELY TO BE PLACED")
    else:
        st.error("⚠️ LOW PLACEMENT PROBABILITY")

st.divider()
st.caption("Model: Random Forest Classifier trained on student performance data.")