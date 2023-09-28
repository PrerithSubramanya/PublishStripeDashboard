import streamlit as st
import requests

import json

st.title("Publish Stripe to Terminal Locations")

# Using the secrets in the app
api_key = st.secrets["api_key"]
device_group_key = st.secrets["device_group_key"]
device_group_value = st.secrets["device_group_value"]

# User input for the location ID
location_id = st.text_input("Enter the terminal location ID:")

# Button to trigger the API call
if st.button("Publish APP"):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2020-08-27; terminal_deploy_api_beta=v1"
    }
    data = {
        f"device_deploy_groups[{device_group_key}]": device_group_value
    }
    response = requests.post(
        f"https://api.stripe.com/v1/terminal/locations/{location_id}",
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 200:
        st.success("Successfully fetched location details!")
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code}")
        st.write(response.text)
