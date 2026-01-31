import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Vijay's Smart Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    color: #4B0082;
}
.sidebar .sidebar-content {
    background-color: #111827;
    color: white;
}
.stButton>button {
    background-color: #4B0082;
    color: white;
    border-radius: 10px;
    height: 45px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Menu")
menu = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📊 Data Dashboard", "📁 Upload CSV", "🤖 ML Demo"]
)

st.sidebar.markdown("---")
st.sidebar.success("Created by Vijayadharshan❤️")

# ------------------ HOME PAGE ------------------
if menu == "🏠 Home":
    st.title("🚀 Welcome to Vijay's Smart Streamlit App")
    st.subheader("Creative • Interactive • Beginner Friendly")

    col1, col2, col3 = st.columns(3)

    col1.metric("Users", "1,245", "+120")
    col2.metric("Projects", "18", "+3")
    col3.metric("Accuracy", "94%", "+2%")

    st.markdown("### 🌈 What this app can do?")
    st.write("""
    - 📊 Interactive data visualization  
    - 📁 Upload & explore CSV files  
    - 🤖 Simple Machine Learning demo  
    - 🎨 Clean & modern UI  
    """)

# ------------------ DATA DASHBOARD ------------------
elif menu == "📊 Data Dashboard":
    st.title("📊 Interactive Data Dashboard")

    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Sales": np.random.randint(100, 500, 5)
    })

    st.dataframe(data, use_container_width=True)

    fig, ax = plt.subplots()
    ax.plot(data["Day"], data["Sales"], marker="o")
    ax.set_title("Weekly Sales Trend")
    ax.set_ylabel("Sales")
    ax.set_xlabel("Day")

    st.pyplot(fig)

# ------------------ CSV UPLOAD ------------------
elif menu == "📁 Upload CSV":
    st.title("📁 Upload Your CSV File")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.success("File uploaded successfully!")

        st.dataframe(df, use_container_width=True)

        st.markdown("### 📈 Column Statistics")
        st.write(df.describe())

# ------------------ ML DEMO ------------------
elif menu == "🤖 ML Demo":
    st.title("🤖 Simple ML Prediction Demo")

    st.markdown("### 🎯 Predict Result (Demo)")

    hours = st.slider("Study Hours", 0, 10, 5)
    sleep = st.slider("Sleep Hours", 0, 10, 6)

    score = (hours * 8) + (sleep * 4)

    if st.button("Predict"):
        st.success(f"🎉 Predicted Score: **{score} / 100**")

        if score > 70:
            st.balloons()
