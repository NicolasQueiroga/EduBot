import streamlit as st

st.set_page_config(
    page_title="EduBot App",
    page_icon="🚀",
    layout="wide",
)

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="font-size: 2.5em;">Welcome to <span style="color: #0066cc;">EduBot App</span> 🚀</h1>
        <p style="font-size: 1.2em; color: #555;">
            Your one-stop solution for document-based interaction and quiz generation.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 📄 Chat with Your Data
        - Upload PDF documents.
        - Ask questions about their content.
        - Get AI-powered answers instantly.
        """
    )
    st.image(
        "https://via.placeholder.com/400x200?text=Chat+with+Your+Data",
        use_container_width=True,
    )

with col2:
    st.markdown(
        """
        ### 📝 Quiz Generator
        - Upload a document (PDF).
        - Generate a quiz on a specified topic.
        - Great for educators and students.
        """
    )
    st.image(
        "https://via.placeholder.com/400x200?text=Quiz+Generator",
        use_container_width=True,
    )

with col3:
    st.markdown(
        """
        ### 🃏 Flashcards Generator
        - Upload a document (PDF).
        - Specify a topic for flashcards.
        - Learn key concepts interactively.
        """
    )
    st.image(
        "https://via.placeholder.com/400x200?text=Flashcards+Generator",
        use_container_width=True,
    )

st.markdown(
    """
    <hr style="margin-top: 40px; margin-bottom: 20px;">
    <footer style="text-align: center; color: #aaa;">
        <p>© 2024 EduBot. Powered by OpenAI and LangChain.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
