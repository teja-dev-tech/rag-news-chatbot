# rag_chain.py

import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import JinaEmbeddings

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "chroma_db")

# 1. Init Jina Embeddings
embedding_model = JinaEmbeddings(jina_api_key=os.getenv("JINA_API_KEY"))

# 2. Load ChromaDB as retriever
vectorstore = Chroma(
    collection_name="news",
    embedding_function=embedding_model,
    persist_directory=CHROMA_DB_DIR,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. Gemini Model via Langchain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.4
)

# 4. Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
)

def get_rag_answer(query: str) -> str:
    """Takes a user query, runs RAG, and returns Gemini answer."""
    try:
        result = qa_chain({"query": query})
        return result.get("result", "Sorry, I couldn't generate a response. Please try again.")
    except Exception as e:
        print(f"Error in get_rag_answer: {str(e)}")
        return "Sorry, I encountered an error while processing your request. Please try again later."
