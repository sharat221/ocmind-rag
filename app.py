import os
import tempfile
import time

import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader, TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

st.set_page_config(page_title="DocMind RAG Assistant", page_icon="📚", layout="wide")

# --------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------


def get_embeddings(api_key: str):
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=api_key)


def get_api_key(user_value: str = "") -> str:
    """Priority: platform secret -> env var -> sidebar input."""
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass
    return os.getenv("GOOGLE_API_KEY", "") or user_value

