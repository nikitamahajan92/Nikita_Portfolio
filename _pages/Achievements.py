import streamlit as st
import pandas as pd

st.title("Achievements & Certifications")

# --- AWARDS SECTION ---
st.subheader("🏆 Awards")
st.markdown("""
<div style="background-color: #1f2937; padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
    <ul style="color: #eee; font-size: 16px;">
        <li>🏅 Selected among Top 10 All India teams and received a prize at the <b>International Robotics Championship, IIT Delhi</b>.</li>
        <li>🎯 Participated in <b>Project Expo 2024</b> and <b>Project Competition</b> with a Computer Vision–based innovative project.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- CERTIFICATIONS SECTION ---
st.subheader("📜 Certifications")
st.markdown("""
<div style="background-color: #374151; padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
    <ul style="color: #eee; font-size: 16px;">
        <li>☁️ <b>Microsoft Azure AI Fundamentals</b> – Microsoft (Aug 11, 2023)</li>
        <li>🧠 Attended Microsoft Workshop: <b>Maximizing AI Potential with Azure & ChatGPT</b> (May 19, 2023)</li>
        <li>🚀 Completed <b>24 ISRO–IIRS Online Certifications</b> under the guidance of ISRO</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- ISRO–IIRS CERTIFICATIONS TABLE ---
st.subheader("🛰 ISRO–IIRS Certification List")

cert_data = [
    ["2020610143048", "61", "Satellite Photogrammetry and its Application", "ISRO–IIRS", "29-06-2020 - 03-07-2020", "Online", "Dr. Anil Kumar / Dr. Hina Pandey"],
    ["2020600157683", "60", "Application of Geoinformatics in Ecological Studies", "ISRO–IIRS", "13-07-2020 - 24-07-2020", "Online", "Dr. Hitendra Padalia"],
    ["2020630178284", "60", "RS Applications in Agricultural Water Management", "ISRO–IIRS", "03-08-2020 - 07-08-2020", "Online", "Dr. Poonam S Tiwari"],
    ["2020640330611", "64", "Basics of Remote Sensing GIS and GNSS", "ISRO–IIRS", "17-08-2020 - 20-11-2020", "Online", "Dr. Poonam Seth"],
    ["2020650330671", "65", "Remote Sensing and Digital Image Analysis", "ISRO–IIRS", "17-08-2020 - 11-09-2020", "Online", "Ms. Minakshi Kumar"],
    ["2020660349495", "66", "Global Navigation Satellite System", "ISRO–IIRS", "14-09-2020 - 25-09-2020", "Online", "Dr. Ashutosh Bhardwaj"],
    ["2020670367917", "67", "Understanding of Coastal Ocean Processes", "ISRO–IIRS", "21-09-2020 - 25-09-2020", "Online", "Dr. A. K. Mishra"],
    ["2020680367949", "68", "Geographical Information System", "ISRO–IIRS", "28-09-2020 - 23-10-2020", "Online", "Mr. Prasun Kumar"],
    ["2020720513120", "72", "Basics of Geocomputation and Geoweb Services", "ISRO–IIRS", "19-10-2020 - 29-10-2020", "Online", "Dr. Harish Karnatak / Mr. Kamal Pandey"],
    ["2020690456252", "69", "RS & GIS Applications", "ISRO–IIRS", "26-10-2020 - 20-11-2020", "Online", "Dr. C.M. Bhatt"],
    ["2020710562725", "71", "Advances in SAR-Polarimetry & Interferometry", "ISRO–IIRS", "14-12-2020 - 18-12-2020", "Online", "Dr. Anil Kumar"],
    ["IIRS20201011588742", "1011", "Space Technology and its Applications", "ISRO–IIRS", "11-01-2021", "Online", "Mr. Kamal Pandey"],
    ["IIRS202073590018", "73", "Overview of Geoprocessing using Python", "ISRO–IIRS", "18-01-2021 - 29-01-2021", "Online", "Mr. Ravi Bhandari"],
    ["20216001901083", "6001", "Space Tech & Applications for School Teachers", "ISRO–IIRS", "31-05-2021 - 04-06-2021", "Online", "Dr. Harish Karnatak"],
    ["202182997714", "82", "Machine Learning to Deep Learning", "ISRO–IIRS", "05-07-2021 - 09-07-2021", "Online", "Dr. Anil Kumar"],
    ["202110171116723", "1017", "Workshop on SAR for Flood Mapping", "ISRO–IIRS", "16-07-2021", "Online", "Dr. Arijit Roy"],
    ["2021851183594", "85", "Basics of RS GIS & GNSS", "ISRO–IIRS", "16-08-2021 - 26-08-2021", "Online", "Dr. Poonam Seth"],
    ["202110151116676", "1015", "Lunar Remote Sensing & Applications", "ISRO–IIRS", "11-08-2021", "Online", "Dr. Mamta Chauhan"],
    ["2020620178266", "92", "Geospatial Inputs for Master Plan", "ISRO–IIRS", "11-10-2021 - 14-10-2021", "Online", "Dr. Pramod Kumar"],
    ["2022981517098", "98", "AI for EO and Geodata Handling", "ISRO–IIRS", "02-05-2022 - 13-05-2022", "Online", "Dr. Sameer Saran"],
    ["202210221526878", "1022", "Planetary Exploration of the Moon", "ISRO–IIRS", "20-05-2022", "Online", "Dr. Poonam S Tiwari"],
    ["2023118186727", "118", "ML Applications in Urban Studies", "ISRO–IIRS", "05-06-2023 - 09-06-2023", "Online", "Dr. Sandeep Maithani / Dr. Surendra Sharma"],
    ["2023500819209", "5008", "Geoprocessing using Python (WgCAPD)", "ISRO–IIRS", "17-07-2023 - 28-07-2023", "Online", "Mr. Ravi Bhandari"],
    ["202330011920899", "3001", "Overview of Space Science", "ISRO–IIRS", "20-07-2023 - 20-08-2023", "Online", "Dr. Harish Karnatak"]
]

columns = [
    "Registration No", "Course No", "Course Name",
    "Vendor", "Duration", "Mode", "Course Coordinator"
]

# Create DataFrame
df = pd.DataFrame(cert_data, columns=columns)

# Custom table style with light hover effect
st.markdown("""
<style>
thead tr th {
    background-color: #1f2937;
    color: white;
}
tbody tr:hover {
    background-color: #374151;
}
tbody td {
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# Show the table
st.dataframe(df, use_container_width=True)
