from PIL import Image
import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader

website_icon = Image.open("images/website_home_page_icon.png")

st.set_page_config(
    page_title="CapConnect",
    page_icon=website_icon
)

st.sidebar.success("Select a page above.")

def user_entry_page(name):
    st.write("# Welcome to CapConnect! 👋")
    st.write(f'Welcome *{name}*')
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        CapConnect is a tool for assisting cancer patients and their families.
    """
    )
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

def med_staff_entry_page(name):
    st.write("# Welcome to Medical CapConnect! 👋")
    st.write(f'Welcome *{name}*')
    st.title('Medical staff page')
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        CapConnect is a tool for assisting cancer patients and their families.
    """
    )


st.set_page_config(
    page_title="CapConnect",
    # page_icon="👋",
)


with open('Database/users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'],
)



name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.session_state["user_type"] = config['credentials']['usernames'][username]['user_type']
    if st.session_state["user_type"] == 'user':
        user_entry_page(name)
    elif st.session_state["user_type"] == 'med_staff':
        med_staff_entry_page(name)


elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')


