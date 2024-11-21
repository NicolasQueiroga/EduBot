import streamlit as st

st.set_page_config(page_title="Flashcards Generator", page_icon="🃏", layout="wide")


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


def generate_flashcards(text, topic):
    prompt = PromptTemplate(
        input_variables=["text", "topic"],
        template=(
            "Based on the following content:\n\n{text}\n\n"
            "Create 10 flashcards on the topic of '{topic}'. Each flashcard should have a 'Question' "
            "and 'Answer' format, focusing on key concepts or details relevant to the topic. Ensure "
            "the flashcards are concise and informative."
        ),
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text": text, "topic": topic})


st.sidebar.title("📤 Upload Document")
uploaded_file = st.sidebar.file_uploader(
    "Upload a document (PDF) to generate flashcards:",
    type="pdf",
)

st.title("🃏 Flashcards Generator")
st.write("Upload a document and specify a topic to generate flashcards.")

if uploaded_file:
    file_path = documents_path / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        file_path = f.name

    st.info("Extracting text from the document...")
    pages = extract_text_from_pdf(file_path)
    if not pages:
        st.warning(
            "The uploaded document is empty or could not be processed. Please try a different file."
        )
    else:
        document_text = " ".join([page.page_content for page in pages])
        st.success(f"Document loaded successfully with {len(pages)} page(s)!")

        topic = st.text_input(
            "Enter a topic for the flashcards:",
            placeholder="E.g., Machine Learning, World War II, Photosynthesis",
        )

        if st.button("Generate Flashcards"):
            if not topic.strip():
                st.warning("Please enter a topic to generate flashcards.")
            elif len(document_text) < 100:
                st.warning(
                    "The document content is too short to generate meaningful flashcards. Please upload a more detailed document."
                )
            else:
                with st.spinner("Generating your flashcards..."):
                    flashcards = generate_flashcards(document_text, topic)
                    if "flashcards" not in flashcards.lower():
                        st.warning(
                            "Unable to generate meaningful flashcards. Please try a different topic or provide a more detailed document."
                        )
                    else:
                        st.success("Flashcards generated successfully!")
                        st.write(flashcards)

                        flashcards_bytes = BytesIO()
                        flashcards_bytes.write(flashcards.encode("utf-8"))
                        flashcards_bytes.seek(0)

                        st.download_button(
                            label="Download Flashcards",
                            data=flashcards_bytes,
                            file_name="generated_flashcards.txt",
                            mime="text/plain",
                        )

st.markdown(
    """
    <hr style="margin-top: 40px; margin-bottom: 20px;">
    <footer>
        <p style="text-align: center;">© 2024 EduBot. Powered by OpenAI and LangChain.</p>
    </footer>
""",
    unsafe_allow_html=True,
)
