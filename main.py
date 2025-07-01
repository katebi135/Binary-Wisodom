import streamlit as st
from jafr_module import name_to_number, get_jafr_insight
from moon_logic import calculate_lunar_phase
from simiyya_module import get_simiyya_reading
from kimiya_module import get_kimiya_profile
from limiyya_module import get_limiyya_astro
import datetime

st.set_page_config(page_title="Abrahamic Reading Portal", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.write("Experience esoteric readings based on sacred numerology, Qur’anic wisdom, and Abrahamic traditions.")

with st.form("reading_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Full Name")
    father_name = st.text_input("Father's Full Name")

    name_birth = st.date_input("Your Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31))
    mother_birth = st.date_input("Mother's Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31))
    father_birth = st.date_input("Father's Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31))

    children_input = st.text_area("Children's Names and DOBs (One per line: Name - YYYY-MM-DD)")

    submit = st.form_submit_button("📖 Get Your Reading")

if submit:
    st.success("✅ Reading complete. Scroll down to see your insights.")

    # Calculate abjad value and insights
    name_value = name_to_number(name)
    mother_value = name_to_number(mother_name)
    jafr_result = get_jafr_insight(name_value, mother_value)

    st.subheader("🧮 Jafr (Islamic Numerology)")
    st.json(jafr_result)

    st.subheader("🜁 Simiyya (Symbolic Reading)")
    st.json(get_simiyya_reading(name))

    st.subheader("⚗ Kimiya (Spiritual Chemistry)")
    st.json(get_kimiya_profile(name_value))

    st.subheader("🪐 Limiyya (Astrology & Qur'anic Wisdom)")
    st.json(get_limiyya_astro(name_birth))
