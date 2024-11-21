import streamlit as st

st.set_page_config(page_title="Quiz Generator", page_icon="📝", layout="wide")


import os
from io import BytesIO
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEY not found. Please set it in your environment variables.")
    st.stop()

documents_path = Path("documents")
documents_path.mkdir(exist_ok=True)

st.markdown(
    """
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #004d99;
        }
    </style>
""",
    unsafe_allow_html=True,
)

llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o-mini",
    openai_api_key=openai_api_key,
)


def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load_and_split()


def generate_quiz(text, topic):
    prompt = PromptTemplate(
        input_variables=["text", "topic"],
        template=(
            "Based on the following content:\n\n{text}\n\n"
            "Create a quiz with 5 multiple-choice questions on the topic of '{topic}'. "
            "Each question should have 4 answer options and the correct answer marked. "
            "Make sure the questions are relevant to the topic and are of moderate difficulty. "
            "Provide the correct answer in brackets like this: [Correct Answer: Option X]."
        ),
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text": text, "topic": topic})


st.sidebar.title("📤 Upload Document")
uploaded_file = st.sidebar.file_uploader(
    "Upload a document (PDF) to generate a quiz:",
    type="pdf",
)

st.title("📝 Quiz Generator")
st.write("Upload a document and specify a topic to generate a quiz.")

if uploaded_file:
    file_path = documents_path / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        file_path = f.name

    st.info("Extracting text from the document...")
    pages = extract_text_from_pdf(file_path)
    document_text = " ".join([page.page_content for page in pages])
    st.success("Document loaded successfully!")

    topic = st.text_input(
        "Enter a topic for the quiz:",
        placeholder="E.g., Algebra, Geometry, Probability",
    )

    if st.button("Generate Quiz"):
        if topic.strip():
            with st.spinner("Generating your quiz..."):
                quiz = generate_quiz(document_text, topic)
                st.success("Quiz generated successfully!")
                st.write(quiz)

                # Convert quiz text to a downloadable format
                quiz_bytes = BytesIO()
                quiz_bytes.write(quiz.encode("utf-8"))
                quiz_bytes.seek(0)

                # Add a download button for the quiz
                st.download_button(
                    label="Download Quiz",
                    data=quiz_bytes,
                    file_name="generated_quiz.txt",
                    mime="text/plain",
                )
        else:
            st.warning("Please enter a topic to generate the quiz.")

st.markdown(
    """
    <hr style="margin-top: 40px; margin-bottom: 20px;">
    <footer>
        <p style="text-align: center;">© 2024 EduBot. Powered by OpenAI and LangChain.</p>
    </footer>
""",
    unsafe_allow_html=True,
)
