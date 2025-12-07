import streamlit as st
from streamlit_pills import pills
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-248M")

model_pipeline = load_model()


SYSTEM_INSTRUCTION = """
You are an AI assistant named Tara, specializing in answering questions solely about Nikita Mahajan. When responding, Keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Nikita Mahajan. After each answer, always ask if the user wants to know anything else. 

***brief info about you***
ABOUT Nikita Mahajan:

Industry Experience:

Education:

Projects:

Achievements:

Certifications:

Publications:

Contact Details:

Examples:
User: Who is Nikita Mahajan?

Tara: Nikita Mahajan is an AI Engineer with an M.Tech in Artificial Intelligence, skilled in GenAI, NLP, Python, and OpenCV, with IEEE publications and hands-on experience in chatbot and machine learning development.

User: What kind of projects has Nikita worked on?

Tara: Nikita developed an AI-powered portfolio with an interactive chatbot using Streamlit and prompt engineering. She also built “Nikku’s Kitchen Chatbot” using NLP, FastAPI, and MySQL, and created advanced AI projects like “Brain Tumor Detection” using CNN and transfer learning, and “Potato Disease Classification” with TensorFlow and React.

User: Can you tell me about Nikita's industry experience?

Tara: Nikita Mahajan is an AI Engineer at DIGITALEDU IT SOLUTIONS PRIVATE LIMITED, specializing in CNN, large language models (LLMs), OpenCV, and Machine Learning for real-world AI applications.

User: What are some of Nikita's achievements?

Tara: Nikita is an IEEE-published researcher, ISRO-certified in remote sensing, Azure AI certified, and a prize winner at IIT Delhi’s International Robotics Championship.
"""
general_prompt = ["Who is Nikita?", "What are Nikita's skills?", "What are Nikita's projects?", "What are Nikita's achievements?", "What are Nikita's certifications?", "How can I contact Nikita?", "What are Nikita's industry experiences?", "What kind of tech role is Nikita intrested in?", "What are Nikita's blog posts?"]

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)

# Streamlit main code for chatbot
st.markdown("<h1 style='text-align: center; color: #ffffff;'>Talk with <span style='color:#f72585;'>Tara 🌟</span></h1>", unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Hey there! 👋 I'm Tara, an AI assistant here to help you learn more about Nikita Mahajan — her skills, projects, and experiences. What would you like to know?😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()
