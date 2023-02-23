import streamlit as st
import requests
import os
from streamlit_lottie import st_lottie
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Home", page_icon=":tada:")


# ----- LOAD ASSETS ----- #



# ----- HEADER SECTION ------ #



def load_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_url(f"https://assets3.lottiefiles.com/packages/lf20_hrkmmhjf.json")

# Use local csss

def css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

css("style/style.css")
with st.container():
    st.subheader("Hello, I am Callum :wave:")
    st.title("A programmer from the UK")
    st.write("If I want something, I make it.")

# -----  MY PROJECTS  ------ #

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Projects")
        st.write("\n")
        st.write("""
Some of the programs that I've made:

- Meross Light Controller.
- Discord Application Command Bot with a ticket system.
- Portscanners, Network Scanner.
- Android Debub Bridge POC.
- And many more.
 
If you want to see more projects or contact me, consider joining my [Discord Server](https://discord.gg/QFPqrYWWDs).""")
with right_column:
    st_lottie(lottie, height=300, key="coding")



# ----- CONTACT ---------


with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("\n")

    contact_form = f"""
    <form id="contactform" action="https://formsubmit.io/send/calcunningham44@icloud.com" method="POST">
        <input type="hidden" name="_captcha" value="false>
        <input name="name" type="text" id="name", placeholder="First Name" required>
        <input name="email" type="email" id="email"placeholder="Email Address" required>
        <textarea name="message" placeholder="Your message goes here!" required></textarea>
        <button type="submit">Send Message</button>
    </form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()