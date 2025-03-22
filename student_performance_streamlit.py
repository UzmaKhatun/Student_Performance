import streamlit as st
import numpy as np
import pickle
import joblib

# Load the model
with open('performance.pkl', 'rb') as file:
    model = joblib.load(file)

# 🎯 Page Layout
st.set_page_config(page_title="Student Performance Checker", layout="wide")

# 🎉 Title and Header
st.title('📊 Student Performance Checker')
st.markdown("### Check your Performance Index with ease!")


hr_std = st.number_input("📚 Studied Hours", min_value=0.0, max_value=24.0, step=0.5)
pr_scr = st.number_input("📈 Previous Score", min_value=0, max_value=100, step=1)
sp_ppr = st.number_input("📝 Sample Papers Solved", min_value=0, max_value=50, step=1)
hr_slp = st.number_input("😴 Sleep Hours", min_value=0.0, max_value=24.0, step=0.5)
activi = st.selectbox('⚽ Extracurricular Activity', ['Yes', 'No'])

# 🛠️ Converting button selection to binary values
num_0 = 1 if activi == 'No' else 0
num_1 = 1 if activi == 'Yes' else 0

# 💡 Prediction
data_input = [hr_std, pr_scr, hr_slp, sp_ppr, num_0, num_1]

if st.button('🚀 Check Performance'):
    pred = model.predict([data_input])
    
    # Using metric display for a clean look
    st.success("✅ Prediction Completed!")
    st.metric(label="📊 Performance Index", value=f"{round(pred[0], 2)}")
