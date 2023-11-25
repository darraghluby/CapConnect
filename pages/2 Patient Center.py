import base64

import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_star_rating import st_star_rating

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

st.set_page_config(page_title="Patient Information")

st.markdown("# Patient Feedback and Information")
st.sidebar.header("Mapping Demo")
st.write(
    """This is the Patient Feedback and Information Center, please choose an option in the sidebar"""
)

if st.sidebar.button('Give my feedback'):
    stars = st_star_rating(label="Please rate you experience with <Treatment Name>"
                           , maxValue=10
                           , defaultValue=0, key="rating1",
                           dark_theme=False
                           )
    stars = st_star_rating(label="Please rate you experience with <Hospital Name>"
                           , maxValue=10
                           , defaultValue=0, key="rating2",
                           dark_theme=False
                           )
    stars = st_star_rating(label="Please rate you experience with <Consultant Name>"
                           , maxValue=10
                           , defaultValue=0, key="rating3",
                           dark_theme=False
                           )

if st.sidebar.button('Information Center'):
    displayPDF("/home/djk/Downloads/Paxman-Patient-Brochure-US-WEB.pdf")
