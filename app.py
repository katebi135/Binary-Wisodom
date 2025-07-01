import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Experience esoteric readings based on sacred numerology, Qur’anic wisdom, and Abrahamic traditions.")

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Full Name")
    father_name = st.text_input("Father's Full Name")
    dob = st.date_input("Your Date of Birth")
    mother_dob = st.date_input("Mother's Date of Birth")
    father_dob = st.date_input("Father's Date of Birth")
    children = st.text_area("Children's Names and DOBs (One per line: Name - YYYY-MM-DD)")
    submit = st.form_submit_button("Get Your Reading")

if submit:
    st.success("🕯️ Reading complete. Scroll down to see your insights.")

    def simple_abjad(name):
        abjad_table = {
            'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7,
            'ح': 8, 'ط': 9, 'ی': 10, 'ک': 20, 'ل': 30, 'م': 40,
            'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
            'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
            'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
        }
        return sum(abjad_table.get(ch, 0) for ch in name if ch in abjad_table)

    abjad_value = simple_abjad(name)
    st.write(f"🔢 Abjad Value of Your Name: **{abjad_value}**")

    verse_index = abjad_value % 6236 + 1
    st.write(f"📖 Suggested Qur’anic Verse Number: **{verse_index}**")

    hikma_list = [
        "The worth of every man is in his attainment.",
        "Patience is of two kinds: patience over what pains you, and patience against what you covet.",
        "He who has a thousand friends has not a friend to spare, and he who has one enemy will meet him everywhere."
    ]
    hikma = random.choice(hikma_list)
    st.write(f"🪶 Wisdom from Imam Ali (ع): _{hikma}_")

    st.markdown("---")
    st.caption("© Abrahamic Reading - All rights reserved. Educational use only.")