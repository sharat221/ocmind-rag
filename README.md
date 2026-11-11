# 📚 DocMind – RAG Document Assistant

An AI assistant that answers questions and summarizes your own documents
using Retrieval-Augmented Generation (RAG), with source citations to
reduce hallucinations.

## Features
- Upload PDF, TXT and DOCX files
- Chat with your documents; answers cite the file and page
- Says "I couldn't find that" when the answer isn't in the documents
- Executive summaries, structured summaries and flashcards
- Select a page range to summarize a specific section

## Tech stack
- Streamlit (web UI)
- LangChain (RAG pipeline)
- FAISS (vector database)
- Google Gemini (embeddings and LLM)

## How it works
1. Documents are parsed and split into overlapping chunks.
2. Chunks are embedded and stored in FAISS.
3. A question retrieves the top-k similar chunks.
4. Gemini answers using only those chunks, with citations.

## Run locally
pip install -r requirements.txt
export GOOGLE_API_KEY=your_key
streamlit run app.py

## Deployment
Deployed on Streamlit Community Cloud. The API key is stored as
a secret named GOOGLE_API_KEY, never in the code.

## Privacy note
Document text is sent to Google's Gemini API to generate answers.# ocmind-rag