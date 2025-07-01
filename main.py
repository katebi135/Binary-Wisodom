
import streamlit as st
from datetime import date
from modules.abjad import calculate_abjad
from modules.utils import generate_date_range

st.set_page_config(page_title="Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Portal")

with st.form("user_form"):
    name = st.text_input("Full Name")
    mother_name = st.text_input("Mother's Name")
    dob = st.date_input("Your Date of Birth", min_value=date(1925, 1, 1), max_value=date.today())
    mother_dob = st.date_input("Mother's Date of Birth", min_value=date(1925, 1, 1), max_value=date.today())
    father_name = st.text_input("Father's Name")
    father_dob = st.date_input("Father's Date of Birth", min_value=date(1925, 1, 1), max_value=date.today())
    children = st.text_area("Children's Names and Birthdates (e.g. Ali - 2012-05-01)")
    submit = st.form_submit_button("Get Reading")

if submit:
    st.subheader("📜 Reading Output")
    st.write("🔢 Abjad Value:", calculate_abjad(name))
    st.write("📅 Date Range Preview:", generate_date_range())
    st.success("Your esoteric profile has been generated.")
    st.caption("Disclaimer: For educational and entertainment purposes only.")
