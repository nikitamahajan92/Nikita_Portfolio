# from streamlit_pills import pills
# import json
# # Function to load a JSON file

# with open(r'data/technical_skills.json') as file:
#     description = json.load(file)

# right_column, left_column = st.columns([2, 1])
# with right_column:
#     st.title("Techincal Skills")
#     skills = [
#         "Microservices",
#         "Large Language Model (LLM)",
#         "Small Language Model (SLM)",
#         "Fine Tuning",
#         "Vector Database",
#         "Prompt Engineering",
#         "Docker",
#         "Kubernetes",
#         "RabbitMQ",
#         "Orchestration",
#         "Golang",
#         "MongoDB",
#         "API",
#         "Data Mining",
#         "Data Analytics",
#         "JSON",
#         "Python/R",
#         "Data Visualization",
#         "Orange Framework",
#         "Jupyter Notebook",
#         "Excel",
#         "Machine Learning Algorithms",
#         "Automation",
#         "ETL Pipeline",
#         "Azure Cloud Architecture",
#         "Azure Security Engineering",
#         "Azure Monitor",
#         "Virtual Machine",
#         "Virtual Networks",
#         "Cosmos DB",
#         "Disaster Recovery",
#         "Azure Firewall and Defender",
#         "Azure Functions",
#         "Azure Blueprints",
#         "Open-source Intelligence (OSINT)",
#         "Splunk",
#         "Microsoft Azure Active Directory",
#         "MITRE ATT&CK",
#         "Active Directory",
#         "Architecture",
#         "Auditing",
#         "Azure",
#         "Bash",
#         "Blue Team",
#         "Cisco",
#         "Cloud",
#         "Cloud Systems & Endpoints Active Directory Management",
#         "Cryptography and Encryption Tools",
#         "Network and System Scanning Tools",
#         "Code",
#         "Compliance",
#         "Containers",
#         "Cryptosystems",
#         "Defender",
#         "Encryption",
#         "GitLab",
#         "Linux",
#         "Lynis",
#         "Metasploit",
#         "NIST",
#         "Policy",
#         "PowerShell",
#         "Python",
#         "Red Team",
#         "Reporting",
#         "Sentinel",
#         "SIEM",
#         "Splunk",
#         "Strategy",
#         "Technical Writing",
#         "Unix",
#         "VPN",
#         "Vulnerability Assessment",
#         "Window Server",
#     ]
#     selected = pills("Select a category", skills)
# with left_column:
#     st.title("Description")
#     for skill in description["skills"]:
#         if selected==skill["name"]:
#             st.markdown(skill["description"])

















import streamlit as st
from streamlit_pills import pills
import json

st.set_page_config(page_title="Technical Skills | Nikita Mahajan", layout="wide")

# Load skill descriptions from JSON
with open("data/technical_skills.json") as file:
    description = json.load(file)

# Define layout columns
right_column, left_column = st.columns([2, 1])

# --- Skill List ---
skills = [
    "Python", "Machine Learning Algorithms", "Deep Learning", "OpenCV", "NLP",
    "Large Language Models (LLMs)", "Generative AI", "Prompt Engineering",
    "FastAPI", "Streamlit", "Docker", "GitHub", "Data Analytics",
    "Data Visualization", "MongoDB", "ETL Pipeline", "Jupyter Notebook",
    "Azure Cloud", "Vector Databases", "Chatbot Development",
    "Google Gemini API", "Flask", "Linux", "Cybersecurity Basics",
    "PowerShell", "JSON", "Excel", "REST APIs", "Supervised & Unsupervised Learning","Neural Networks & CNNs", "RNNs & LSTMs","Transformers",
    "Text Classification","Transfer Learning","Scikit-learn","PyTorch / TensorFlow","Hugging Face Transformers","XGBoost / LightGBM",
    "Pandas","Power BI", "Flask","Node.js","Database Design","PostgreSQL / MySQL","HTML / CSS / JavaScript","React.js",
    "NumPy", "Matplotlib", "Seaborn", "Plotly","Git & GitHub","Postman","VS Code / PyCharm","Linux CLI"
]

# --- UI Right Column ---
with right_column:
    st.title("Technical Skills")
    selected = pills("Select a Skill", skills)

# --- UI Left Column ---
with left_column:
    st.title("Description")
    found = False
    for skill in description["skills"]:
        if selected == skill["name"]:
            st.markdown(skill["description"])
            found = True
            break
    if not found and selected:
        st.info(f"No description available for **{selected}** yet.")
