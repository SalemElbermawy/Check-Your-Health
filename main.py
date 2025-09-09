import streamlit as st
import numpy as np

st.markdown(
    """
    <style>
    .stTextInput, .stNumberInput, .stSelectbox, .stSlider {
        padding: 8px;
        border-radius: 12px;
        box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.15);
        font-weight: 500;
    }

    .basic {background-color: #e6f0ff; padding:12px; border-radius:12px; margin-bottom:10px;}
    .live {background-color: #e0f7fa; padding:12px; border-radius:12px; margin-bottom:10px;}
    .habits {background-color: #e8f5e9; padding:12px; border-radius:12px; margin-bottom:10px;}
    .diet {background-color: #fff3e0; padding:12px; border-radius:12px; margin-bottom:10px;}
    .mental {background-color: #f3e5f5; padding:12px; border-radius:12px; margin-bottom:10px;}
    .tests {background-color: #fce4ec; padding:12px; border-radius:12px; margin-bottom:10px;}
    .result-box {background-color: #f9f9f9; padding:10px; border-radius:10px; margin:6px 0; box-shadow:0px 0px 4px rgba(0,0,0,0.1);}

    .stMarkdown h1, .stMarkdown h2 {
        text-shadow: 1px 1px 3px rgba(0,0,0,0.25);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Health Check App")

st.markdown(
    """
    ### 👋 Welcome to Your Health Check
    This tool helps you **track your basic health indicators** including:
    - Body Mass Index (BMI)  
    - Vital Signs (Blood Pressure, Heart Rate, Temperature)  
    - Lifestyle Habits (Sleep, Activity, Smoking, Alcohol)  
    - Nutrition & Diet  
    - Mental Health  
    - Common Lab Tests  

    ⚠️ **Note:** This is a **screening tool only**.  
    It does not replace professional medical advice.  
    If you get abnormal results, please consult your doctor.
    """
)

st.markdown('<div class="basic">', unsafe_allow_html=True)
st.subheader("🆔 Basic Information")
name = st.text_input("👤 Enter your name")
tall = st.number_input("📏 Enter your height (cm)", min_value=50, max_value=250)
weight = st.number_input("⚖ Enter your weight (kg)", min_value=3, max_value=1500)
Gender = st.selectbox("🚻 Gender", options=["👨 Male", "👩 Female"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="live">', unsafe_allow_html=True)
st.subheader("🧬 Vital Signs")
pressure = st.number_input("🩸 Blood Pressure (mmHg)")
heart_rate = st.number_input("❤️ Heart Rate (bpm)")
sugar_level = st.number_input("🧪 Blood Sugar Level (mg/dL)")
chol = st.number_input("🥓 Cholesterol Level (mg/dL)")
temp = st.number_input("🌡 Body Temperature (°C)", min_value=25, max_value=45, step=1)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="habits">', unsafe_allow_html=True)
st.subheader("💤 Habits")
hours = st.number_input("🛌 Sleeping Hours", step=1)
quality_sleep = st.selectbox("😴 Sleep Quality", options=["Bad", "Normal", "Good"])
active_hours = st.slider("🏃 Active Hours per Day", max_value=24, min_value=0, step=1)
daily_steps = st.number_input("👟 Daily Steps", min_value=0, step=100)
smoke = st.selectbox("🚬 Do you smoke?", options=["Yes", "No"])
drink = st.selectbox("🍷 Do you drink alcohol?", options=["Yes", "No"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="diet">', unsafe_allow_html=True)
st.subheader("🥗 Diet")
meals_per_day = st.number_input("🍽 Number of Meals per Day")
amount_water = st.number_input("💧 Water Intake (liters/day)")
veg_fru = st.selectbox("🥦 Fruits & Vegetables Intake", options=["High", "Normal", "Low"])
sugar_consum = st.selectbox("🍬 Sugar Consumption", options=["High", "Normal", "Low"])
fastFood_consum = st.selectbox("🍔 Fast Food Consumption", options=["High", "Normal", "Low"])
caf_consum = st.selectbox("☕ Caffeine Intake", options=["High", "Normal", "Low"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="mental">', unsafe_allow_html=True)
st.subheader("🧠 Mental Health")
stress_level = st.selectbox("😖 Stress Level (0–10)", options=np.arange(0, 11))
global_mood = st.selectbox("😊 Mood Status", options=["Happy", "Neutral", "Depressed"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="tests">', unsafe_allow_html=True)
st.subheader("🧪 Lab Tests")
creatinine = st.number_input("🧬 Creatinine (mg/dL)", min_value=0.0, step=0.1)
urea = st.number_input("🧬 Urea (mg/dL)", min_value=0.0, step=0.1)
alt = st.number_input("🩸 ALT / SGPT (U/L)", min_value=0.0, step=1.0)
ast = st.number_input("🩸 AST / SGOT (U/L)", min_value=0.0, step=1.0)
bilirubin = st.number_input("🧪 Bilirubin (mg/dL)", min_value=0.0, step=0.1)
hb = st.number_input("🩸 Hemoglobin (g/dL)", min_value=0.0, step=0.1)
vitd = st.number_input("☀️ Vitamin D (ng/mL)", min_value=0.0, step=0.1)
iron = st.number_input("🧲 Iron (µg/dL)", min_value=0.0, step=1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.header("📋 Results")

def show_result(text):
    st.markdown(f'<div class="result-box">{text}</div>', unsafe_allow_html=True)

if tall > 0 and weight > 0:
    height_m = tall / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        status = "Underweight 🟦"
    elif 18.5 <= bmi < 25:
        status = "Normal ✅"
    elif 25 <= bmi < 30:
        status = "Overweight 🟨"
    elif 30 <= bmi < 35:
        status = "Obese I 🟧"
    elif 35 <= bmi < 40:
        status = "Obese II 🟥"
    else:
        status = "Obese III 🔴"
    show_result(f"📊 **BMI:** {bmi:.2f} → {status}")

if pressure > 0:
    if pressure < 120:
        bp_status = "Normal ✅"
    elif 120 <= pressure < 140:
        bp_status = "Pre-Hypertension ⚠️"
    elif 140 <= pressure < 160:
        bp_status = "Hypertension Stage 1 ❗"
    else:
        bp_status = "Hypertension Stage 2 🚨"
    show_result(f"🩸 **Blood Pressure:** {bp_status}")

if heart_rate > 0:
    if 60 <= heart_rate <= 100:
        hr_status = "Normal ✅"
    elif heart_rate < 60:
        hr_status = "Bradycardia ⚠️"
    else:
        hr_status = "Tachycardia ❗"
    show_result(f"❤️ **Heart Rate:** {hr_status}")

if sugar_level > 0:
    if sugar_level < 100:
        sugar_status = "Normal ✅"
    elif 100 <= sugar_level < 126:
        sugar_status = "Prediabetes ⚠️"
    else:
        sugar_status = "Diabetes ❗"
    show_result(f"🧪 **Blood Sugar:** {sugar_status}")

if chol > 0:
    if chol < 200:
        chol_status = "Normal ✅"
    elif 200 <= chol < 240:
        chol_status = "Borderline ⚠️"
    else:
        chol_status = "High ❗"
    show_result(f"🥓 **Cholesterol:** {chol_status}")

if temp > 0:
    if 36 <= temp <= 37.5:
        temp_status = "Normal ✅"
    elif temp < 36:
        temp_status = "Hypothermia ⚠️"
    elif 37.5 < temp <= 38.5:
        temp_status = "Mild Fever 🤒"
    elif 38.5 < temp <= 39.5:
        temp_status = "Fever ❗"
    else:
        temp_status = "High Fever 🚨"
    show_result(f"🌡 **Temperature:** {temp_status}")

if hours > 0:
    if hours < 5:
        show_result("🛌 **Sleep:** Very Low ⚠️")
    elif 5 <= hours <= 8:
        show_result("🛌 **Sleep:** Normal ✅")
    else:
        show_result("🛌 **Sleep:** High (possible oversleeping) ⚠️")

if daily_steps > 0:
    if daily_steps < 5000:
        show_result("👟 **Activity:** Low ⚠️")
    elif 5000 <= daily_steps < 10000:
        show_result("👟 **Activity:** Moderate ✅")
    else:
        show_result("👟 **Activity:** High 💪")

if smoke == "Yes":
    show_result("🚬 Smoking is harmful ❌")
if drink == "Yes":
    show_result("🍷 Alcohol may cause health risks ❌")

if amount_water > 0:
    if amount_water < 2:
        show_result("💧 **Water Intake:** Low ⚠️")
    else:
        show_result("💧 **Water Intake:** Good ✅")


if veg_fru == "Low":
    show_result("🥦 **Vegetables/Fruits Intake:** Needs improvement ⚠️")
if sugar_consum == "High":
    show_result("🍬 **Sugar Intake:** High ❌")
if fastFood_consum == "High":
    show_result("🍔 **Fast Food:** Too much ❌")

if stress_level >= 7:
    show_result("⚠️ **High Stress Level** – consider relaxation techniques.")
if global_mood == "Depressed":
    show_result("😟 **Mood Status:** Seek support if needed.")

if creatinine > 0:
    if creatinine <= 1.2:
        show_result("🧬 **Creatinine:** Normal ✅")
    else:
        show_result("🧬 **Creatinine:** High (Possible kidney issue) ❗")

if hb > 0:
    if hb < 12:
        show_result("🩸 **Hemoglobin:** Low (Anemia) ⚠️")
    elif 12 <= hb <= 16:
        show_result("🩸 **Hemoglobin:** Normal ✅")
    else:
        show_result("🩸 **Hemoglobin:** High ❗")
