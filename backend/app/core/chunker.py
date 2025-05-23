import re
import json
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict, Tuple

def clean_text(text: str) -> str:
    """
    Clean text by removing unwanted characters and formatting
    
    Args:
        text: Raw text to clean
        
    Returns:
        Cleaned text
    """
    # Remove newlines and extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters and punctuation
    text = re.sub(r'[\-–—]', ' ', text)  # Replace dashes with spaces
    text = re.sub(r'[\[\]"\']', '', text)  # Remove quotes and brackets
    text = re.sub(r'\n', ' ', text)  # Remove newlines
    
    # Remove BBC-specific patterns
    text = re.sub(r'For more stories.*?sign up.*?newsletter', '', text, flags=re.DOTALL)
    text = re.sub(r'\-\-.*?$', '', text, flags=re.DOTALL)  # Remove trailing signature
    
    # Strip leading/trailing whitespace
    return text.strip()

def save_cleaned_article(article: Dict, directory: str = "cleaned_articles"):
    """
    Save cleaned article as JSON file
    
    Args:
        article: Article dictionary
        directory: Directory to save the file
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Clean the maintext
    cleaned_text = clean_text(article['maintext'])
    
    # Update article with cleaned text
    cleaned_article = article.copy()
    cleaned_article['maintext'] = cleaned_text
    cleaned_article['article_length'] = len(cleaned_text)
    
    # Create filename using article ID
    filename = os.path.join(directory, f"article_{article['article_id']}.json")
    
    # Save article as JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cleaned_article, f, indent=4, ensure_ascii=False)

def split_and_save_articles(articles: List[Dict]) -> List[Tuple[str, Dict]]:
    """
    Split articles into chunks and save cleaned articles
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        List of (chunk_text, metadata) tuples
    """
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    for article in articles:
        if not article.get('maintext'):
            continue
            
        # Save cleaned article
        save_cleaned_article(article)
        
        # Clean the text before splitting
        cleaned_text = clean_text(article['maintext'])
        text_chunks = splitter.split_text(cleaned_text)
        
        metadata = {
            'title': article['title'],
            'url': article['url'],
            'source': article['source_domain'],
            'date': article['date_publish'],
            'article_id': article['article_id']
        }
        
        for chunk in text_chunks:
            # Clean each chunk individually
            cleaned_chunk = clean_text(chunk)
            if cleaned_chunk.strip():  # Only add non-empty chunks
                chunks.append((cleaned_chunk, metadata))
    
    print(f"Created {len(chunks)} cleaned chunks")
    return chunks
