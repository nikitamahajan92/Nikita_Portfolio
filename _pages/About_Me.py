# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/nikita.png", use_container_width=True)

with left_column:
    st.title("About Me")
    st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; line-height: 1.6;'>
        Hello! I’m <b>Nikita Mahajan</b>, an AI Engineer driven by curiosity, creativity, and the power of intelligent technology. 
        With a strong foundation in <b>Python, Machine Learning, OpenCV</b>, and <b>Generative AI</b>, I design and build solutions that bridge innovation with real-world impact.
        <br><br>
        Currently working at <b>DIGITALEDU IT SOLUTIONS PVT LTD</b>, I specialize in developing smart applications using <b>LLMs, image processing,</b> and chatbot frameworks. 
        I hold a <b>Master's degree in Artificial Intelligence</b>, and my academic work has been published through <b>IEEE</b> — reflecting my passion for research and cutting-edge technologies.
        <br><br>
        Whether it’s crafting seamless user experiences or building secure, scalable systems, I’m always excited by the challenge of solving complex problems. 
        Outside the code editor, Outside of work, I enjoy cooking 🍳, reading books 📚, and traveling to new places ✈️ — always seeking inspiration beyond the screen.
        <br><br>
        Thank you for visiting my portfolio. Let’s connect and imagine the future of AI — together 🤖✨
    </div>
    """,
    unsafe_allow_html=True
    
    )
    st.markdown(
        "<div style='text-align: justify;'>"
        "<br>"
        "<a href='https://www.linkedin.com/in/nikita-mahajan-40a481129/' target='_blank'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/nikitamahajan92' target='_blank'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:mahajannikita92@gmail.com'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
    
