import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader


def user_entry_page(name):
    st.write("# Welcome to CapConnect! 👋")
    st.write(f'Welcome *{name}*')
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        CapConnect is a tool for assisting cancer patients and their families.
    """
    )

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


