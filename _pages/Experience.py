# import streamlit as st

# st.set_page_config(page_title="Experience | Nikita Mahajan", layout="wide")
# st.title("Work Experience")

# # --- DigitalEdu ---
# with st.expander("DIGITAL EDU IT SOLUTIONS PRIVATE LIMITED | AI Engineer (Aug 2025 – Present)", expanded=True):
#     st.markdown("""
#     - Developing LLM-based educational solutions.
#     - Leading GenAI and Image Processing projects using OpenCV and Gemini.
#     - Deploying smart AI applications using Streamlit and FastAPI.
#     """)
#     st.code("AI, Machine Learning, JavaScript, Python, OpenCV, LLMs, FastAPI, Gemini, NLP, GitHub")

# # --- VPM Polytechnic ---
# with st.expander("V.P.M's Polytechnic, Thane | Lecturer (Dec 2020 – Feb 2022)"):
#     st.markdown("""
#     - Delivered lectures and labs in electronics and embedded systems.
#     - Guided diploma student projects and supported academic development.
#     """)
#     st.code("Electronics, Robotics, Embedded Systems, Teaching, Project Guidance")

# # --- VnVCS ---
# with st.expander("VnVCS, Navi Mumbai | Trainee Programmer (Nov 2018 – Feb 2019)"):
#     st.markdown("""
#     - Built and supported ASP.NET MVC web applications.
#     - Worked on frontend/backend logic for internal tools.
#     """)
#     st.code("ASP.Net, MVC, HTML, CSS, SQL Server, Visual Studio")


# st.divider()
# st.title("Internship Experience")

# # --- Techoctanet ---
# with st.expander("Techoctanet Services Pvt Ltd | Python Developer Intern (May 2024 – Aug 2024)", expanded=True):
#     st.markdown("""
#     - Built backend logic and modular automation tools in Python.
#     - Participated in app design and REST API integration.
#     """)
#     st.code("Python, Flask, REST API, Git, NumPy, Pandas, Data Analysis")

# # --- CodeClause ---
# with st.expander("CodeClause Pvt Ltd | Data Science Intern (Aug 2023 – Sept 2023)"):
#     st.markdown("""
#     - Worked on GenAI models for text summarization and sentiment analysis.
#     - Built simple data-driven NLP apps.
#     """)
#     st.code("Python, Generative AI, NLP, Sentiment Analysis, Data Science, Machine Learning")

# # --- Exposys Data Labs ---
# with st.expander("Exposys Data Labs | Data Science Intern (July 2023 – Aug 2023)"):
#     st.markdown("""
#     - Built robotics automation and chatbots for real-time tasks.
#     - Explored AI + IoT integration.
#     """)
#     st.code("Python, Chatbots, Data Science, CNN, Machine Learning")



import streamlit as st

st.set_page_config(page_title="Experience | Nikita Mahajan", layout="wide")
st.title("Work Experience")

# Define a reusable function for styled blocks
def experience_card(title, duration, responsibilities, tech_stack, color="#1f2937"):
    st.markdown(f"""
        <div style="background-color: {color}; padding: 1.3rem; border-radius: 12px; margin-bottom: 1rem;">
            <h4 style="color: white;"> {title}</h4>
            <p style="color: #bbb;"><b>Duration:</b> {duration}</p>
            <ul style="color: #aaa; line-height: 1.6;">
                {''.join([f"<li>{task}</li>" for task in responsibilities])}
            </ul>
            <p style="color: #ccc;"><b>Tech Stack:</b> <code>{tech_stack}</code></p>
        </div>
    """, unsafe_allow_html=True)


# --- Work Experience ---
experience_card(
    "DIGITAL EDU IT SOLUTIONS PRIVATE LIMITED | AI Engineer",
    "Aug 2025 – Present",
    [
        "Developing LLM-based educational solutions.",
        "Leading GenAI and Image Processing projects using OpenCV and Gemini.",
        "Deploying smart AI applications using Streamlit and FastAPI."
    ],
    "AI, Machine Learning, JavaScript, Python, OpenCV, LLMs, FastAPI, Gemini, NLP, GitHub",

)

experience_card(
    "V.P.M's Polytechnic, Thane | Lecturer",
    "Dec 2020 – Feb 2022",
    [
        "Delivered lectures and labs in electronics and embedded systems.",
        "Guided diploma student projects and supported academic development."
    ],
    "Electronics, Robotics, Embedded Systems, Teaching, Project Guidance",

    color="#374151"
)

experience_card(
    "VnVCS, Navi Mumbai | Trainee Programmer",
    "Nov 2018 – Feb 2019",
    [
        "Built and supported ASP.NET MVC web applications.",
        "Worked on frontend/backend logic for internal tools."
    ],
    "ASP.Net, MVC, HTML, CSS, SQL Server, Visual Studio",
    
    color="#4b5563"
)

# Divider
st.markdown("""<hr style="border: 1px solid #444;">""", unsafe_allow_html=True)

st.title("Internship Experience")

# --- Internships ---
experience_card(
    "Techoctanet Services Pvt Ltd | Python Developer Intern",
    "May 2024 – Aug 2024",
    [
        "Built backend logic and modular automation tools in Python.",
        "Participated in app design and REST API integration."
    ],
    "Python, Flask, REST API, Git, NumPy, Pandas, Data Analysis",
    
)

experience_card(
    "CodeClause Pvt Ltd | Data Science Intern",
    "Aug 2023 – Sept 2023",
    [
        "Worked on GenAI models for text summarization and sentiment analysis.",
        "Built simple data-driven NLP apps."
    ],
    "Python, Generative AI, NLP, Sentiment Analysis, Data Science, Machine Learning",
   
    color="#374151"
)

experience_card(
    "Exposys Data Labs | Data Science Intern",
    "July 2023 – Aug 2023",
    [
        "Built robotics automation and chatbots for real-time tasks.",
        "Explored AI + IoT integration."
    ],
    "Python, Chatbots, Data Science, CNN, Machine Learning",
    
    color="#4b5563"
)
