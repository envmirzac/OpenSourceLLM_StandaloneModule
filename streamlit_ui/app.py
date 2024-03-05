import streamlit as st
import requests
import os

# Setting page config to wide mode
st.set_page_config(layout="wide")

# Title and description
st.title('Interactive LLM Processor')
st.markdown("""
    Welcome to the interactive Large Language Model processor. 
    Enter your message and let the AI amaze you with its response!
""")

# Retrieve API URL from environment variables, default to localhost if not found
api_url = os.getenv('API_URL', 'http://localhost:8000')

# Sidebar for user input
with st.sidebar:
    st.header('Compose your message here')
    message = st.text_area('Enter your message:', height=150)
    process_button = st.button('Process')

# Using columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('Your Message')
    st.write(message)

if process_button and message:
    with col2:
        with st.spinner('Processing...'):
            # Make the POST request to the API service
            response = requests.post(f'{api_url}/process/', json={"content": message})
            if response.status_code == 200:
                processed_message = response.json()['processed_content']
                st.subheader('Processed Message')
                st.write(processed_message)
            else:
                st.error(f"Failed to process message: {response.reason}")

# Footer
st.markdown("---")
st.markdown("ℹ️ This app is powered by Streamlit and communicates with an LLM backend to process your messages.")
