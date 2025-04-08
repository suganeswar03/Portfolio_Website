import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage-Suganeswar Savadamuthu", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#use Local CSS file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

lottie_coding = load_lottieurl("https://lottie.host/e84ec03a-115f-4d9a-8abb-7ee677f9b6ae/fkzC6ZnB98.json")
Picturec = Image.open("images/Picturec.png")
Pictureb = Image.open("images/Pictureb.png")
Pictured = Image.open("images/Pictured.png")


#header section
with st.container():
    st.subheader("Hi, Iam Suganeswar Savadamuthu :wave:")
    st.title("Cybersecurity Engineer")
    st.write("Masters Graduate @ Pace University,Newyork.")
    st.write("Gmail: suganeswar2000@gmail.com")
    st.write("Mobile: +91 9942645560")
    st.write("[Linkedin >]https://www.linkedin.com/in/suganeswar-savadamuthu-069097153")


#what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """ Cybersecurity professional with 1 year of experience in security best practices, vulnerability assessments, and incident response. Skilled in automation scripting, security monitoring, and risk mitigation, with hands-on expertise in SIEM, EDR, penetration testing, and cloud security. Proficient in Python programming with practical experience in developing security solutions. Adept at securing infrastructure, enforcing security policies, and integrating security controls. Experienced in agile environments, ensuring efficient and adaptive security implementations"""
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
# work experience
with st.container():
    st.write("---")
    st.header("Work Experience")
    st.subheader("**Cybersecurity Engineer - Intern** | **humanID** | **New York, USA**  \n**June 2024 – April 2025**")
    st.write(
        """
        - Assisted in implementing security best practices by automating security policies and monitoring compliance.  
        - Developed security automation scripts in Python to detect and respond to threats, improving response time by 40%.  
        - Conducted vulnerability assessments and penetration testing, identifying and mitigating security risks.  
        - Monitored network traffic and system logs using SIEM tools (Splunk, QRadar) to detect suspicious activities.  
        - Engaged in incident response efforts by analyzing security breaches, implementing fixes, and documenting lessons learned.  
        - Assisted in security patching and managing updates to protect systems against known vulnerabilities.  
        - Collaborated with cross-functional teams to enforce security compliance with frameworks such as ISO 27001 and SOC 2.  
        - Researched emerging security threats and provided recommendations to improve defense mechanisms.  
        - Assisted in setting up security monitoring dashboards to visualize threats and security incidents.  
        """
    )

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Pictureb)

    with text_column:
        st.subheader("Autonomous Security Monitoring & Incident Response.")
        st.write("""I have designed a python programme that will trigger an email, if a new service starts running on 
        the host. I have used psutil and smtp packages for this programme.""")
        st.markdown("[Learn More...](https://github.com/suganeswar03/python_project/tree/17379599f2b12223912ba0d0c3d2c5c3cbe4b320)")

#project2
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Picturec)

    with text_column:
        st.subheader("Portfolio Website Using Python")
        st.write("""I have designed a python programme to create a portfolio Website with the help of Streamlit.""")
        st.markdown("[Learn More...](https://github.com/suganeswar03/Portfolio_Website.git)")

#project3
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Pictured)

    with text_column:
        st.subheader("Cloud Security Metrics & Risk Analysis")
        st.write(""" I have focused on two specific metrics that would contribute significantly to the 
evaluation of cloud security for corporations: Privileged Access Monitoring and Configuration 
Security Score. This research paper deals with these metrics to contribute to the understanding 
of cloud security risks and liabilities for corporations. """)




#contact form

    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """<form action="https://formsubmit.co/suganeswar2000@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name"required>
             <input type="email" name="email" placeholder="Your email"required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()





    



