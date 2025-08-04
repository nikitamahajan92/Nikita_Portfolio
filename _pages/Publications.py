import streamlit as st

st.set_page_config(page_title="Publications | Nikita Mahajan", layout="wide")
st.title("Research Publications")

# Load PDF files
with open("data/5. MRI_Images_Based_Brain_Tumor_Detection_Using_CNN_for_Multiclass_Classification.pdf", "rb") as f1:
    pdf1 = f1.read()

with open("data/4. A_Robust_Approach_for_Brain_Tumor_Detection_using_Transfer_Learning.pdf", "rb") as f2:
    pdf2 = f2.read()

# Styled publication card
def publication_card(conference, location, publisher, date, title, doi, link, pdf_data, filename, color="#1f2937"):
    st.markdown(f"""
    <div style="background-color: {color}; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.2rem;">
        <h4 style="color: white;">{conference}</h4>
        <p style="color: #bbb;"><b>📍 Location:</b> {location}</p>
        <p style="color: #bbb;"><b>📅 Date:</b> {date}</p>
        <p style="color: #bbb;"><b>📚 Publisher:</b> {publisher}</p>
        <p style="color: #ddd;"><b>📝 Title:</b> {title}</p>
        <p style="color: #ccc;"><b>🔗 DOI:</b> <a href="https://doi.org/{doi}" target="_blank" style="color: #f72585;">{doi}</a></p>
        <p>
            🌐 <a href="{link}" target="_blank" style="text-decoration: none; color: #f72585;"><b>View on IEEE Xplore</b></a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download PDF",
        data=pdf_data,
        file_name=filename,
        mime="application/pdf",
        use_container_width=True
    )
    st.markdown("---")


# --- Publication 1: ASIANCON ---
publication_card(
    conference="2023 3rd Asian Conference on Innovation in Technology (ASIANCON)",
    location="Ravet IN, India",
    publisher="IEEE",
    date="August 25–27, 2023",
    title="MRI Images Based Brain Tumor Detection Using CNN for Multiclass Classification",
    doi="10.1109/ASIANCON58793.2023.10270492",
    link="https://ieeexplore.ieee.org/document/10270492",
    pdf_data=pdf1,
    filename="ASIANCON_MRI_Tumor_Classification.pdf",
    color="#1f2937"
)

# --- Publication 2: ICIRCA ---
publication_card(
    conference="2023 5th International Conference on Inventive Research in Computing Applications (ICIRCA)",
    location="Coimbatore, India",
    publisher="IEEE",
    date="August 3–5, 2023",
    title="A Robust Approach for Brain Tumor Detection Using Transfer Learning",
    doi="10.1109/ICIRCA57980.2023.10220906",
    link="https://ieeexplore.ieee.org/document/10220906",
    pdf_data=pdf2,
    filename="ICIRCA_Transfer_Learning_Brain_Tumor.pdf",
    color="#374151"
)
