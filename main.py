
import streamlit as st
from jafr_module import name_to_number, get_jafr_insight
from moon_logic import calculate_lunar_phase
from simiyya_module import get_simiyya_reading
from kimiya_module import get_kimiya_profile
from limiyya_module import get_limiyya_astro
from datetime import datetime

st.set_page_config(page_title="Abrahamic Reading Portal", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.write("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

with st.form("reading_form"):
    name = st.text_input("Full Name")
    name_birth = st.date_input("Date of Birth")

    mother_name = st.text_input("Mother's Name")
    mother_birth = st.date_input("Mother's Date of Birth")

    father_name = st.text_input("Father's Name")
    father_birth = st.date_input("Father's Date of Birth")

    child1_name = st.text_input("Child 1 Name")
    child1_birth = st.date_input("Child 1 DOB")

    child2_name = st.text_input("Child 2 Name")
    child2_birth = st.date_input("Child 2 DOB")

    location = st.text_input("Place of Birth")

    submit = st.form_submit_button("🔵 Generate Reading")

if submit:
    st.success("📜 Reading generated below.")
    name_value = name_to_number(name)
    mother_value = name_to_number(mother_name)

    jafr_result = get_jafr_insight(name_value, mother_value)
    st.subheader("📘 Jafr (Islamic Numerology)")
    st.json(jafr_result)

    st.subheader("🧿 Simiyya (Symbolic Reading)")
    st.json(get_simiyya_reading(name))

    st.subheader("⚗️ Kimiya (Spiritual Chemistry)")
    st.json(get_kimiya_profile(name_birth))

    st.subheader("🌙 Limiyya (Astrology & Quranic Wisdom)")
    st.json(get_limiyya_astro(name_birth))
