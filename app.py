import streamlit as st
import requests

# Secrets se details uthana
APP_ID = st.secrets["APP_ID"]
APP_SECRET = st.secrets["APP_SECRET"]
REDIRECT_URI = "https://fbtokengenerator-csjam4sw4kuwjghquihjm4.streamlit.app/" 

st.title("🚀 FB Token Extractor")

# Login URL
login_url = f"https://www.facebook.com/v18.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope=public_profile,email"

if st.button("Login with Facebook"):
    st.markdown(f'[Authorize Karne Ke Liye Yahan Click Karein]({login_url})', unsafe_allow_html=True)

# Token nikalne ka logic
if "code" in st.query_params:
    code = st.query_params["code"]
    url = f"https://graph.facebook.com/v18.0/oauth/access_token?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&client_secret={APP_SECRET}&code={code}"
    res = requests.get(url).json()
    
    if "access_token" in res:
        st.success("Mubarak ho! Aapka Token niche hai:")
        st.code(res["access_token"])
    else:
        st.error("Galti: " + str(res.get('error', {}).get('message')))
