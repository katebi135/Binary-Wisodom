import streamlit as st
from jafr_module import name_to_number, get_jafr_insight
from moon_logic import calculate_lunar_phase
from simiyya_module import get_simiyya_reading
from kimiya_module import get_kimiya_profile
from limiyya_module import get_limiyya_astro
from datetime import datetime, date

from hijri_converter import convert
from convertdate import jalali

# Set page title
st.set_page_config(page_title="Abrahamic Reading Portal", layout="centered")

st.title("📜 Abrahamic Reading Portal")
st.write("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

# Set date range (100 years back from today)
today = date.today()
min_date = today.replace(year=today.year - 100)

with st.form("reading_form"):
    name = st.text_input("Full Name")
    name_birth = st.date_input("Date of Birth", min_value=min_date, max_value=today)

    mother_name = st.text_input("Mother's Name")
    mother_birth = st.date_input("Mother's Date of Birth", min_value=min_date, max_value=today)

    father_name = st.text_input("Father's Name")
    father_birth = st.date_input("Father's Date of Birth", min_value=min_date, max_value=today)

    child1_name = st.text_input("Child 1 Name")
    child1_birth = st.date_input("Child 1 DOB", min_value=min_date, max_value=today)

    child2_name = st.text_input("Child 2 Name")
    child2_birth = st.date_input("Child 2 DOB", min_value=min_date, max_value=today)

    location = st.text_input("Place of Birth (Optional)")

    submit = st.form_submit_button("🔮 Generate Reading")

if submit:
    st.success("✅ Reading generated below.")

    name_value = name_to_number(name)
    mother_value = name_to_number(mother_name)
    jafr_result = get_jafr_insight(name_value, mother_value)

    st.subheader("🔢 Jafr (Islamic Numerology)")
    st.write(f"Abjad Value of Your Name: **{name_value}**")
    st.json(jafr_result)

    st.subheader("🌙 Simiyya (Symbolic Reading)")
    st.json(get_simiyya_reading(name))

    st.subheader("🧪 Kimiya (Spiritual Chemistry)")
    st.json(get_kimiya_profile(name_value))

    st.subheader("🌌 Limiyya (Astrology & Qur'anic Wisdom)")
    st.json(get_limiyya_astro(name_birth))

    # Optional: Show multi-calendar formats
    hijri = convert.Gregorian(name_birth.year, name_birth.month, name_birth.day).to_hijri()
    shamsi = jalali.from_gregorian(name_birth.year, name_birth.month, name_birth.day)

    st.markdown(f"📆 **Gregorian**: {name_birth.strftime('%Y-%m-%d')}")
    st.markdown(f"🕋 **Hijri**: {hijri.year}-{hijri.month}-{hijri.day}")
    st.markdown(f"🌞 **Shamsi**: {shamsi[0]}-{shamsi[1]}-{shamsi[2]}")
