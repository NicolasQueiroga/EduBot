import streamlit as st

st.set_page_config(page_title="Chat with Your Data", page_icon="📄", layout="wide")


import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
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
        .chat-container {
            margin: 10px 0;
            padding: 10px;
            border-radius: 10px;
            width: 80%;
            display: inline-block;
        }
        .chat-user {
            background-color: #e6f7ff;
            color: #003366;
            text-align: left;
            float: left;
            margin-bottom: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .chat-bot {
            background-color: #f0f0f0;
            color: #333333;
            text-align: left;
            float: right;
            margin-bottom: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .chat-container p {
            margin: 0;
            padding: 0;
            word-wrap: break-word;
        }
        .clear-both {
            clear: both;
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

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vector_store = None


def load_and_index_pdfs(pdf_paths):
    global vector_store
    docs = []
    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        docs.extend(loader.load_and_split())
    vector_store = FAISS.from_documents(docs, embeddings)
    st.success(f"Indexed {len(docs)} pages from {len(pdf_paths)} PDF(s).")


def get_pdf_response(query):
    if not vector_store:
        st.error(
            "No PDFs indexed. Please upload and index PDFs to enable this feature."
        )
        return "No PDFs available for answering your question."

    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )
    results = retriever.get_relevant_documents(query)

    if not results:
        st.warning(
            "The subject of your question is not covered in the uploaded documents."
        )
        return (
            "I couldn't find any relevant information in the uploaded documents. "
            "You can try rephrasing your question or uploading additional documents."
        )

    st.info("Generating response using context from indexed PDFs.")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)


st.sidebar.title("📤 Upload PDFs")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files to chat with:",
    accept_multiple_files=True,
    type="pdf",
)

if uploaded_files:
    pdf_paths = []
    for uploaded_file in uploaded_files:
        file_path = documents_path / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            pdf_paths.append(f.name)
    load_and_index_pdfs(pdf_paths)

st.title("📄 Chat with Your Data")
st.write("Upload PDF documents and ask questions about their content.")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

query = st.text_input(
    "Ask a question:",
    placeholder="E.g., What does the document say about X?",
    help="Type your question and press Enter to get a response based on the uploaded PDFs.",
)

if query:
    response = get_pdf_response(query)
    st.session_state.chat_history.append({"user": query, "bot": response})

if st.session_state.chat_history:
    st.subheader("📬 Chat History")
    for chat in st.session_state.chat_history:
        if "user" in chat:
            st.markdown(
                f"""
                <div class="chat-container chat-user">
                    <p><strong>You:</strong> {chat['user']}</p>
                </div>
                <div class="clear-both"></div>
            """,
                unsafe_allow_html=True,
            )
        if "bot" in chat:
            st.markdown(
                f"""
                <div class="chat-container chat-bot">
                    <p><strong>Bot:</strong> {chat['bot']}</p>
                </div>
                <div class="clear-both"></div>
            """,
                unsafe_allow_html=True,
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
