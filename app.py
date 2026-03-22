import streamlit as st
import requests

# 1. Sabse pehle check karein ki Secrets load ho rahe hain ya nahi
try:
    APP_ID = st.secrets["APP_ID"]
    APP_SECRET = st.secrets["APP_SECRET"]
except Exception as e:
    st.error("Secrets not found! Please add APP_ID and APP_SECRET in Streamlit Settings.")
    st.stop()

# 2. Redirect URI (Isme koi galti nahi honi chahiye)
REDIRECT_URI = "https://fbtokengenerator-csjam4sw4kuwjghquihjm4.streamlit.app/"

st.title("🚀 FB Token Extractor")

# 3. Login URL generate karna
login_url = f"https://www.facebook.com/v18.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope=public_profile,email"

# Debugging ke liye URL print karke dekhte hain
st.write("---")
st.write("### Step 1: Login")
st.info("Niche wale link par click karein:")
st.markdown(f'[👉 Click here to Login with Facebook]({login_url})')

# 4. Token Exchange Logic
if "code" in st.query_params:
    st.write("### Step 2: Extracting Token...")
    auth_code = st.query_params["code"]
    token_url = f"https://graph.facebook.com/v18.0/oauth/access_token?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&client_secret={APP_SECRET}&code={auth_code}"
    
    res = requests.get(token_url).json()
    
    if "access_token" in res:
        st.success("Mubarak ho! Token mil gaya:")
        st.code(res["access_token"])
    else:
        st.error(f"Error: {res.get('error', {}).get('message')}")
