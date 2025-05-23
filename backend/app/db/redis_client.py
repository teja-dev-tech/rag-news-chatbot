import json
import redis
import os
import glob
from datetime import datetime
from typing import List, Dict, Optional, Any
from pathlib import Path
from ..models.chat import Message
from ..models.article import Article

class RedisManager:
    def __init__(self):
        self.redis = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=int(os.getenv("REDIS_DB", 0)),
            decode_responses=True
        )
        self.ttl = 86400  # 24 hours TTL

    def _get_key(self, session_id: str, suffix: str = "") -> str:
        return f"chat:{session_id}:{suffix}" if suffix else f"chat:{session_id}"

    async def save_message(self, session_id: str, message: str, response: str) -> None:
        """Save user message and bot response to chat history."""
        try:
            # Save messages
            msg_data = [
                Message(role="user", content=message).json(),
                Message(role="assistant", content=response).json()
            ]
            
            # Save to Redis
            key = self._get_key(session_id, "messages")
            self.redis.rpush(key, *msg_data)
            
            # Set TTL
            self.redis.expire(key, self.ttl)
            
        except Exception as e:
            print(f"Redis error: {e}")
            raise

    async def get_chat_history(self, session_id: str) -> List[Dict]:
        """Retrieve chat history for a session."""
        try:
            messages = self.redis.lrange(self._get_key(session_id, "messages"), 0, -1)
            return [json.loads(msg) for msg in messages]
        except Exception as e:
            print(f"Redis error: {e}")
            return []

    async def delete_session(self, session_id: str) -> bool:
        """Delete a session and its chat history."""
        try:
            return bool(self.redis.delete(
                self._get_key(session_id),
                self._get_key(session_id, "messages")
            ))
        except Exception as e:
            print(f"Redis error: {e}")
            return False

    async def get_articles(self) -> List[Dict[str, Any]]:
        """Get all articles from the knowledge base."""
        try:
            articles_dir = Path(__file__).parent.parent.parent / 'cleaned_articles'
            articles = []
            
            if not articles_dir.exists():
                return []
                
            for file_path in articles_dir.glob('*.json'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        article_data = json.load(f)
                        article = {
                            'id': str(article_data.get('id', '')),
                            'title': article_data.get('title', 'Untitled'),
                            'description': article_data.get('description', ''),
                            'url': article_data.get('url', '#'),
                            'date_publish': article_data.get('date_publish', ''),
                            'source_domain': article_data.get('source_domain', 'Unknown')
                        }
                        articles.append(article)
                except json.JSONDecodeError:
                    continue
                    
            return articles
            
        except Exception as e:
            print(f"Error loading articles: {e}")
            return []
            
    async def get_article(self, article_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific article by ID."""
        try:
            articles_dir = Path(__file__).parent.parent.parent / 'cleaned_articles'
            file_pattern = f"*{article_id}*.json"
            
            for file_path in articles_dir.glob(file_pattern):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        article_data = json.load(f)
                        return {
                            'id': str(article_data.get('id', '')),
                            'title': article_data.get('title', 'Untitled'),
                            'description': article_data.get('description', ''),
                            'maintext': article_data.get('maintext', ''),
                            'url': article_data.get('url', '#'),
                            'date_publish': article_data.get('date_publish', ''),
                            'source_domain': article_data.get('source_domain', 'Unknown'),
                            'article_length': article_data.get('article_length', 0)
                        }
                except json.JSONDecodeError:
                    continue
                    
            return None
            
        except Exception as e:
            print(f"Error loading article {article_id}: {e}")
            return None

    async def session_exists(self, session_id: str) -> bool:
        """Check if a session exists."""
        return bool(self.redis.exists(self._get_key(session_id)))

# Global instance
redis_client = RedisManager()
