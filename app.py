
import streamlit as st
from datetime import date

st.set_page_config(page_title="Binary Wisdom", layout="centered")

st.title("🧿 Binary Wisdom: Abrahamic Numerology Portal")
st.markdown("Welcome to the spiritual toolkit built on sacred science and divine tradition.")

today = date.today()
hundred_years_ago = date(today.year - 100, today.month, today.day)

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    dob = st.date_input("Your Date of Birth", value=today, min_value=hundred_years_ago, max_value=today)

    mother_name = st.text_input("Mother's Full Name")
    mother_dob = st.date_input("Mother's Date of Birth", value=today, min_value=hundred_years_ago, max_value=today)

    father_name = st.text_input("Father's Full Name")
    father_dob = st.date_input("Father's Date of Birth", value=today, min_value=hundred_years_ago, max_value=today)

    child_name = st.text_input("Child's Name")
    child_dob = st.date_input("Child's Date of Birth", value=today, min_value=hundred_years_ago, max_value=today)

    submit = st.form_submit_button("🔮 Get My Reading")

if submit:
    st.success("✅ Reading Complete")
    st.info("✨ Disclaimer: For educational and entertainment purposes only.")

st.markdown("---")
st.caption("© Binary Wisdom – All rights reserved.")
