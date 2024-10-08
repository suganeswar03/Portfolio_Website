import streamlit as st

st.header(":mailbox: Get In Touch with Me!")

contact_form = """<form action="https://formsubmit.co/suganeswar2000@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name"required>
     <input type="email" name="email" placeholder="Your email"required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


# use local css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css.txt")

