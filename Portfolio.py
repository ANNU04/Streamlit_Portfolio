import streamlit as st
from PIL import Image
import base64

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="My Portfolio", layout="wide")
    
    # Set background image for all pages
    set_background("BG.jpg")
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Education","Contact"])
    
    if page == "Home":
        home()
    elif page == "Projects":
        projects()
    elif page == "Skills":
        skills()
    elif page == "Education":
        Education()
    elif page == "Contact":
        contact()

def home():
    st.title("👋 Welcome to My Portfolio!")
    st.image("Anant Gupta.jpg", width=350)  # Add your profile image
    st.write("Hello! I'm Anant Gupta, a passionate Data Enthusiast. Here’s a little about me!")
    
    st.markdown("""
    - 🎯 Experienced in Python, Data Science, and Web Development.
    - 💻 Love solving problems and building scalable solutions.
    - 🚀 Always learning new technologies.
    
    **📝 Download my Resume:** [Click Here](Anant-Resume.pdf)
    """)

def projects():
    st.title("📂 My Projects")
    
    project_data = [
        {"name": "Project 1", "desc": "Automatic Pronunciation Mistake Detector using Python", "link": "https://github.com/ANNU04/Automatic-Pronunciation-Mistake-Detector-"},
        {"name": "Project 2", "desc": "Driver Revenue Increasing Analysis (Statistics)", "link": "https://github.com/ANNU04/Statistical-Data-Analysis"},
        {"name": "Project 3", "desc": "Microsoft Data Analysis using Jupyter Notebook", "link": "https://github.com/ANNU04/Microsoft-Data-Analysis"}
    ]
    
    for project in project_data:
        st.subheader(project["name"])
        st.write(project["desc"])
        st.markdown(f"🔗 [View Project]({project['link']})")
        st.write("---")

def skills():
    st.title("💡 Skills & Technologies")
    skilled  = [
        {"name": "Python", "image": "Python.jpg"},
        {"name": "SQL", "image": "Sql.jpg"},
        {"name": "Excel", "image": "Excel.png"},
        {"name": "Power BI", "image": "PowerBI.png"},
        {"name": "Streamlit", "image": "Streamlit.png"},
        {"name": "Azure", "image": "Azure.png"},
        {"name": "Statistics", "image": "Statistics.jpg"},
        {"name": "Time-Series Analysis", "image": "Time Series.png"}
    ]
    
    for skill in skilled:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(skill["image"], width=50)
        with col2:
            st.subheader(skill["name"])
            
def Education():
    st.title("📖 My Education")
    col1, col2, col3 = st.columns(3)  # Corrected columns
    with col1:
        st.subheader("🎓 B.Tech (CSE)")
        st.write("JECRC UNIVERSITY (2021-2025)")
        st.write("CGPA: 9.0")
    with col2:
        st.subheader("🏫 12th Grade")
        st.write("AVMD School (2021)")
        st.write("Score: 75%")
    with col3:
        st.subheader("📚 10th Grade")
        st.write("Holy Public School (2019)")
        st.write("Score: 85%")

        
def contact():
    st.title("📞 Contact Me")
    st.write("Feel free to reach out via the platforms below!")
    
    st.subheader("""
    - 📧 Email: [anantg800@gmail.com](mailto:anantg800@gmail.com) 
    """)
    st.subheader("""
    - 🌟 LinkedIn: [Anant Gupta](https://www.linkedin.com/in/anant-gupta-0a1900221/)
    """)
    st.subheader("""
    - 🔗 GitHub: [ANNU04](https://github.com/ANNU04)
    """)
   

if __name__ == "__main__":
    main()