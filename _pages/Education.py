
import streamlit as st

st.title("Education")

# Define education data
education_data = [
    {
        "institute": "K. J. Somaiya Institute of Technology, Sion, Mumbai",
        "degree": "M.Tech in Artificial Intelligence",
        "university": "Mumbai University",
        "duration": "2021 - 2023",
        # "description": "Gained advanced knowledge in AI, ML, NLP, and worked on cutting-edge research and practical projects.",
        "color": "#1f2937"
    },
    {
        "institute": "Bharati Vidyapeeth College of Engineering, Navi Mumbai",
        "degree": "B.E. in Electronics and Telecommunication",
        "university": "Mumbai University",
        "duration": "2014 - 2017",
        # "description": "Specialized in core electronics subjects with exposure to embedded systems and telecom networks.",
        
        "color": "#374151"
    },
    {
        "institute": "S. H. Mansukhani Institute of Technology, Ulhasnagar",
        "degree": "Diploma in Electronics and Telecommunication",
        "university": "Mumbai University",
        "duration": "2011 - 2014",
        # "description": "Built strong fundamentals in electronics, circuit design, and practical lab work.",
        
        "color": "#4b5563"
    }
]

# Display each education block with styling
for edu in education_data:
    st.markdown(f"""
        <div style="background-color:{edu['color']}; padding: 1.2rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: white;"> {edu['institute']}</h4>
            <p style="color: #ddd; margin: 0.3rem 0;"><strong>Degree:</strong> {edu['degree']}</p>
            <p style="color: #ccc; margin: 0.3rem 0;"><strong>University:</strong> {edu['university']}</p>
            <p style="color: #bbb; margin: 0.3rem 0;"><strong>Duration:</strong> {edu['duration']}</p>
        </div>
    """, unsafe_allow_html=True)

# Optional: spacing fix
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

