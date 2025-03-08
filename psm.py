import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Alisha", page_icon="🔑", layout="centered")
#custom css
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width; 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: black; color: white; font-size: 18px; }
    .stButton button:hover { background-color: red; color: white;}
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("Secure Password Evaluator 🔐")
st.write("Type your password to assess its strength. 🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long ** .")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 Password should include **both upper case (A-Z) and lowercase (a-z) letters** .")

    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("🔢 Password should include **at least one number(0-9)** .")

    #special character
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
       feedback.append(" ⁉ Include **at least one special character (!@#$%^&*)**.") 

    #display password strength result
    if score == 4:
        st.success("✔ **Strong Password** - ✅🔒 Your password is strong and well-protected! 🔐")
    elif score == 3 :
        st.info("**⚠ Moderate Password** - 🔐 Enhance security by adding more features! 🔧")
    else:
        st.error("❕ **Weak Password** - Follow the suggestion below to strength it. ")

    #feedback
    if feedback:
        with st.expander(" **🔑 Strengthen your password for better security! 🔒** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Make sure your password is robust and secure. 🔐")

#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Kindly input a password first. 🔑") #show warning if password empty
