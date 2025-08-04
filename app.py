import streamlit as st
from streamlit_option_menu import option_menu

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Nikita's Portfolio",
    layout="wide",
    initial_sidebar_state="auto",
)

# ---------- SIDEBAR ----------
with st.sidebar:
    choose = option_menu(
        "Nikita Mahajan",
        [
            "Tara",
            "About Me",
            "Experience",
            "Technical Skills",
            "Education",
            "Projects",
            "Achievements",
            "Publications",
            "Blog",
            "Resume",
            "Contact",
        ],
        icons=[
            "robot",
            "person-fill",
            "briefcase-fill",
            "tools",
            "book-fill",
            "kanban-fill",
            "trophy-fill",
            "file-earmark-text",
            "pencil-square",
            "file-earmark-person",
            "envelope-fill",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )

    # ---------- SOCIAL ICONS ----------
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <a href='https://www.linkedin.com/in/nikita-mahajan-40a481129/' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='35'>
            </a>
            &nbsp;&nbsp;
            <a href='https://github.com/nikitamahajan92' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='35'>
            </a>
            &nbsp;&nbsp;
            <a href='mailto:mahajannikita92@gmail.com'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='35'>
            </a>
        </div>
    """, unsafe_allow_html=True)

    # ---------- FOOTER BELOW ICONS ----------
    st.markdown("""
        <hr style="margin-top: 25px; margin-bottom: 10px;">
        <div style='text-align: center; font-size: 12px; color: #888; line-height: 1.4;'>
            Made with ❤️<br>by <b style="color: #f72585;">Nikita Mahajan</b><br>
            © 2025 All rights reserved.
        </div>
    """, unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
pages = {
    "Tara": "_pages/home.py",
    "About Me": "_pages/About_Me.py",
    "Experience": "_pages/Experience.py",
    "Technical Skills": "_pages/technical_skills.py",
    "Education": "_pages/Education.py",
    "Projects": "_pages/Projects.py",
    "Achievements": "_pages/Achievements.py",
    "Publications": "_pages/Publications.py",
    "Blog": "_pages/Blog.py",
    "Resume": "_pages/Resume.py",
    "Contact": "_pages/Contact.py",
}

# ---------- LOAD SELECTED PAGE ----------
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())

# ---------- OPTIONAL: BUTTON HOVER CSS ----------
st.markdown("""
    <style>
    button:hover {
        background-color: #f72585 !important;
        color: white !important;
        border: 1px solid #f72585 !important;
    }
    </style>
""", unsafe_allow_html=True)
