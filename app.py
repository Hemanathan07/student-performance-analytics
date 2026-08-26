import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

st.title("🎓 Student Placement Predictor")
st.write("Enter a student's details to predict placement likelihood.")

@st.cache_resource
def train_model():
    df = pd.DataFrame({
        "attendance": [95,90,85,70,65,92,88,60,78,96,82,55,86,73,91,80],
        "study_hours": [8,7,6,3,2,7,5,2,4,9,5,1,6,3,8,5],
        "average_mark": [90,86,82,60,55,88,76,50,68,94,75,45,84,62,89,72],
        "placed": [1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1]
    })
    df["study_attendance_score"] = df["study_hours"] * df["attendance"] / 100
    X = df.drop(columns="placed")
    y = df["placed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=150, random_state=42))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline

model = train_model()

attendance = st.slider("Attendance (%)", 0, 100, 80)
study_hours = st.slider("Study Hours per day", 0, 12, 5)
average_mark = st.slider("Average Mark", 0, 100, 70)

study_attendance_score = study_hours * attendance / 100

if st.button("Predict Placement"):
    features = pd.DataFrame(
        [[attendance, study_hours, average_mark, study_attendance_score]],
        columns=["attendance", "study_hours", "average_mark",