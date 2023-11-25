import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

FILENAME: str = "Database/users.yaml"


with open(FILENAME, "r", encoding="utf-8") as file:
    config = yaml.load(file, Loader=SafeLoader)

    print(config)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Login', 'main')

print("name")
