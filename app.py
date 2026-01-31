import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Vijay Smart Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6fb;
}
h1, h2, h3 {
    color: #4B0082;
}
.stButton>button {
    background-color: #4B0082;
    color: white;
    border-radius: 10px;
    height: 45px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Select Page",
    ["🏠 Home", "📊 Dashboard", "📁 Upload CSV", "🤖 ML Demo"]
)

st.sidebar.markdown("---")
st.sidebar.success("Created by Vijayadharshan")

# ---------------- HOME ----------------
if menu == "🏠 Home":
    st.title("🚀 Welcome to Vijay's Smart Streamlit App")
    st.subheader("Creative • Interactive • Beginner Friendly")

    col1, col2, col3 = st.columns(3)
    col1.metric("Users", "1,250", "+120")
    col2.metric("Projects", "15", "+3")
    col3.metric("Accuracy", "95%", "+2%")

    st.markdown("### 🌟 App Features")
    st.write("""
    ✔ Interactive Dashboard  
    ✔ CSV Upload & Analysis  
    ✔ Simple ML Demo  
    ✔ Modern UI  
    """)

# ---------------- DASHBOARD ----------------
elif menu == "📊 Dashboard":
    st.title("📊 Sales Dashboard")

    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Sales": np.random.randint(100, 500, 5)
    })

    st.dataframe(data, use_container_width=True)

    st.subheader("📈 Sales Trend")
    st.line_chart(data.set_index("Day"))

# ---------------- CSV UPLOAD ----------------
elif menu == "📁 Upload CSV":
    st.title("📁 Upload CSV File")

    file = st.file_uploader("Upload your CSV file", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.success("✅ File uploaded successfully!")

        st.dataframe(df, use_container_width=True)
        st.subheader("📊 Summary Statistics")
        st.write(df.describe())

# ---------------- ML DEMO ----------------
elif menu == "🤖 ML Demo":
    st.title("🤖 Simple ML Prediction (Demo)")

    st.write("Predict score based on study & sleep hours")

    study_hours = st.slider("📘 Study Hours", 0, 10, 5)
    sleep_hours = st.slider("😴 Sleep Hours", 0, 10, 6)

    predicted_score = (study_hours * 7) + (sleep_hours * 3)

    if st.button("🔮 Predict"):
        st.success(f"🎯 Predicted Score: **{predicted_score} / 100**")
        if predicted_score >= 70:
            st.balloons()
