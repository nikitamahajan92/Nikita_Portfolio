import streamlit as st

st.set_page_config(page_title="Blog | Nikita Mahajan", layout="wide")
st.title("Blog")

# Blog Card
st.markdown("""
    <div style="background-color: #1f2937; padding: 1.5rem; border-radius: 12px; margin-top: 1.2rem;">
        <h4 style="color: #ffffff;">MRI Images Based Brain Tumor Detection Using CNN</h4>
        <p style="color: #bbb;">A detailed walkthrough of how Convolutional Neural Networks (CNN) were used to classify different types of brain tumors from MRI scans.</p>
        <p style="color: #bbb;"><b>Published on:</b> <span style="color: #f72585;">Medium</span></p>
        <a href="https://nikitamahajan92.medium.com/mri-images-based-brain-tumor-detection-using-cnn-c8dcbb705655" target="_blank" style="text-decoration: none;">
            🔗 <span style="color: #25c7ae;"><b>Read Full Blog</b></span>
        </a>
    </div>
""", unsafe_allow_html=True)
