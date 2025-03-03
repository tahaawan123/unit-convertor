import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2f;
            color: #ffffff;
        }
        .stApp {
            background-color: #1e1e2f;
            color: #ffffff;
        }
        .stSelectbox, .stButton, .stNumberInput {
            border-radius: 10px;
            padding: 10px;
            background-color: #2a2a3b;
            color: #ffffff;
            border: 1px solid #4caf50;
        }
        .stButton > button {
            background-color: #4caf50;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with an emoji sticker
st.title("🚀 Unit Converter App")

st.markdown("### 🔄 Convert Length, Weight, and Time Instantly!")
st.write("🌟 Welcome! Select a category to get started.")

category = st.selectbox("📌 Choose a Category", ["Length", "Weight", "Time"])

def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("📝 Enter your value")

if st.button("🔄 Convert"):
    result = convert_unit(category, value, unit)
    st.success(f"✅ {value} {unit} is {result}")
    st.write("🎉 Thanks for using this app!")
