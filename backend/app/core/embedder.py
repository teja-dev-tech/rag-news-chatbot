import os
from typing import List, Dict, Tuple
from dotenv import load_dotenv
from chromadb import PersistentClient
from chromadb.utils.embedding_functions import JinaEmbeddingFunction

load_dotenv()

def embed_and_store(chunks: List[Tuple[str, Dict]]) -> None:
    """
    Store chunks in Chroma DB with embeddings
    
    Args:
        chunks: List of (chunk_text, metadata) tuples
    """
    if not chunks:
        print("No chunks to process")
        return
    
    client = PersistentClient(path=os.getenv("CHROMA_DB_DIR", "chroma_db"))
    
    # Create or get collection
    collection = client.get_or_create_collection(name="news_chunks")
    
    # Prepare data for embedding
    documents = []
    metadatas = []
    ids = []
    
    for i, (text, metadata) in enumerate(chunks):
        if not text.strip():
            continue
            
        # Generate unique ID
        chunk_id = f"chunk_{metadata['article_id']}_{i}"
        
        documents.append(text)
        metadatas.append({
            'title': metadata['title'],
            'url': metadata['url'],
            'source': metadata['source'],
            'date': metadata['date'],
            'article_id': metadata['article_id'],
            'chunk_index': i
        })
        ids.append(chunk_id)
    
    if not documents:
        print("No valid chunks to embed")
        return
    
    print(f"Adding {len(documents)} chunks to Chroma DB")
    
    # Add chunks to collection
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"Total chunks in collection: {collection.count()}")
    print("Example chunk metadata:", metadatas[0] if metadatas else "No metadata")
