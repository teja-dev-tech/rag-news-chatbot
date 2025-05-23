from newsplease import NewsPlease
from typing import List, Dict, Optional

import time
from typing import List, Dict, Optional
from urllib.parse import urlparse

def fetch_article(url: str, max_retries: int = 3, retry_delay: int = 5) -> Optional[Dict]:
    """
    Fetch a single article with retry mechanism
    
    Args:
        url: Article URL
        max_retries: Maximum number of retries
        retry_delay: Delay between retries in seconds
        
    Returns:
        Article dictionary or None if failed
    """
    print(f"Fetching article: {url}")
    
    for attempt in range(max_retries):
        try:
            article = NewsPlease.from_url(url)
            if article and hasattr(article, 'title'):
                # Convert datetime objects to ISO format strings
                date_download = getattr(article, 'date_download', None)
                
                article_dict = {
                    'title': getattr(article, 'title', ''),
                    'description': getattr(article, 'description', ''),
                    'url': url,
                    'maintext': getattr(article, 'maintext', ''),
                    'date_publish': date_download.isoformat() if date_download else None,
                    'source_domain': getattr(article, 'source_domain', '')
                }
                
                # Add article ID based on URL hash
                article_dict['article_id'] = hash(url)
                
                # Add article length
                article_dict['article_length'] = len(article_dict['maintext'])
                
                return article_dict
            
        except Exception as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed for {url}: {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Failed to fetch {url} after {max_retries} attempts")
                return None

def fetch_articles_from_urls(urls: List[str]) -> List[Dict]:
    """
    Fetch articles from multiple URLs with error handling and rate limiting
    
    Args:
        urls: List of article URLs
        
    Returns:
        List of article dictionaries
    """
    article_dicts = []
    
    for url in urls:
        # Add a small delay between requests to avoid rate limiting
        time.sleep(1)
        
        article = fetch_article(url)
        if article:
            article_dicts.append(article)
    
    print(f"\nSuccessfully fetched {len(article_dicts)} out of {len(urls)} articles")
    return article_dicts
