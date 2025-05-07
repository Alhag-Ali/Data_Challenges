import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# ---- Titel der App ----
st.title("Machine Learning Classifier")

# ---- Hochladen der CSV-Datei ----
uploaded_file = st.file_uploader("./data/bw.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:", df.head())

    # ---- Auswahl der Target-Spalte ----
    target_column = st.selectbox("Select Target Column", df.columns)

    # ---- Auswahl der Feature-Spalten ----
    feature_columns = st.multiselect("Select Feature Columns", df.columns, default=[col for col in df.columns if col != target_column])

    # ---- Datenungleichgewicht-Handling ----
    imbalance_handling = st.radio("Select Data Imbalance Handling", ["None", "Undersampling", "Oversampling"], index=0)

    # ---- Button zum Starten des Trainings ----
    if st.button("Train Model"):
        # ---- Daten vorbereiten ----
        X = df[feature_columns]
        y = df[target_column]

        # Umwandlung kategorischer Werte in numerische Werte
        X = pd.get_dummies(X)

        # ---- Train-Test-Split ----
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # ---- Datenungleichgewichtsbehandlung ----
        if imbalance_handling == "Oversampling":
            smote = SMOTE(random_state=42)
            X_train, y_train = smote.fit_resample(X_train, y_train)
        elif imbalance_handling == "Undersampling":
            undersample = RandomUnderSampler(random_state=42)
            X_train, y_train = undersample.fit_resample(X_train, y_train)

        # ---- Modell trainieren ----
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # ---- Klassifikationsbericht anzeigen ----
        report = classification_report(y_test, y_pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose()

        st.subheader("Classification Report")
        st.dataframe(report_df.style.format({"precision": "{:.4f}", "recall": "{:.4f}", "f1-score": "{:.4f}"}))
