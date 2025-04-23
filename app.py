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
    st.title("Data Engineer")
    st.write("Masters Graduate @ Pace University,Newyork.")
    st.write("Gmail: suganeswar2000@gmail.com")
    st.write("Mobile: +91 9342090431")
    st.write("[Linkedin >]https://www.linkedin.com/in/suganeswar-savadamuthu-069097153")


#what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """ Data Engineer with 1 year of experience in Data pipeline development with proven ability to understand      customer requirements and translate into actionable project plans. Strong Python coding with good Hands-on experience and extensive experience working in agile environment."""
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
# work experience
with st.container():
    st.write("---")
    st.header("Work Experience")
    st.subheader("**Data Engineer - Intern** | **humanID** | **New York, USA**  \n**June 2024 – April 2025**")
    st.write(
        """•	Designed, developed, and debugged mission-critical software in an agile Scrum environment, improving functionality by 20% through feature enhancements.
           •	Developed and integrated high-performance RESTful APIs, optimizing data retrieval and reduced latency.
           •	Implemented sensor data processing pipelines to enable real-time analytics and autonomous decision-making.
           •	Ensured software reliability and scalability by conducting peer reviews, reducing production issues by 30%.
           •	Worked with Linux-based environments, troubleshooting and resolving issues to enhance system stability by 15%.
           •	Used GitHub for version control, improving collaboration and accelerating development cycles by 25%.
           •	Developed reusable object-oriented programming (OOP) components, reducing future development time.
           •	Participated in continuous integration (CI/CD) pipelines using Jenkins, ensuring automated deployments with a 50% reduction in downtime.
           •	Engaged in simulation testing to verify system functionality, contributing to a 100% alignment with software verification processes"""
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
        st.write("""I developed a real-time monitoring service for Linux systems to detect and log new background processes. To enhance security, I added automated email alerts for unauthorized service initiations, reducing manual monitoring by 80%. Using multi-threaded processing, I achieved 100% success in anomaly detection and built a lightweight API to integrate alerts with external monitoring tools for improved compliance.""")
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





    



