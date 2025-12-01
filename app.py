import streamlit as st
import requests

st.title("Language Transleter")
text = st.text_area("Enter Your name")

if st.button("Submit"):
    if text:
        response = requests.post(url ="https://shrutikakkapade.app.n8n.cloud/webhook-test/97b0edee-c0f1-4e88-bca1-2b5625e041c4",json={"input":text})
        
        if response.status_code == 200:
            response_data = response.json()
            st.write(response_data["output"])
else:
    pass