from PIL import Image
import streamlit as st

website_icon = Image.open("images/website_home_page_icon.png")

st.set_page_config(
    page_title="CapConnect",
    page_icon=website_icon
)

st.sidebar.success("Select a page above.")

home_page_md = """
# Welcome to CapConnect!

## Mission:

Make the cancer journey more seamless for all stakeholders at all stages of care.

## Target Audience:

Manufacturers of the cold caps (Paxman Scalp Cooling)

## Our Services:

1. **Database Management:**
   - Creating a comprehensive database for monitoring patient health throughout the journey, both pre and post-discharge (Pre-care and Post-care).

2. **Training Programs:**
   - Educating and training programmers for Nurses, Doctors, and Consultants to handle the equipment, specifically cold caps, during and before treatment.

3. **Administrative System:**
   - Modern and smooth administrative system designed to efficiently manage customer data at all stages of the cancer care journey.

4. **Awareness and Education Programs:**
   - Developing awareness and education programs during and post-treatment for support givers, including friends and family members. Ensuring a holistic approach to the cancer support system.

Our goal is to enhance the overall experience for everyone involved in the cancer care process. Through technology, education, and support, Cap-Connect aims to contribute to a more seamless and informed journey for patients, healthcare professionals, and support networks alike.
"""

st.markdown(home_page_md)
