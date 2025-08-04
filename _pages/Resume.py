import streamlit as st

st.set_page_config(page_title="Resume | Nikita Mahajan", layout="wide")
st.title("My Resume")

# Load your resume PDF file (place in 'data/' folder)
with open("/home/abcd/Downloads/Portfolio/Nikita_Portfolio/data/Resume Nikita Mahajan.pdf", "rb") as f:
    resume_bytes = f.read()

# Styled resume card
st.markdown("""
<div style="background-color: #1f2937; padding: 2rem; border-radius: 12px; margin-top: 1.5rem;">
    <h3 style="color: white;">📌 Download My Resume</h3>
    <p style="color: #ccc; font-size: 16px;">
        Want to learn more about my background, skills, and achievements? Download the complete resume here:
    </p>
</div>
""", unsafe_allow_html=True)
st.divider()
# Download button
st.download_button(
    label="⬇️ Download Resume (PDF)",
    data=resume_bytes,
    file_name="Nikita_Mahajan_Resume.pdf",
    mime="application/pdf",
    use_container_width=True
)



