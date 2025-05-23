import uuid
from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from ..core.rag_chain import get_rag_answer
from ..db.redis_client import redis_client
from ..models.chat import ChatRequest, ChatResponse, ChatHistory
from ..models.article import Article
    
chat_router = APIRouter(prefix="/api/chat", tags=["Chat"])
articles_router = APIRouter(prefix="/api/articles", tags=["Articles"])

@articles_router.get(
    "",
    response_model=List[dict],
    summary="Get list of articles",
    description="Retrieve list of articles in the knowledge base"
)
async def get_articles():
    """Get list of articles in the knowledge base."""
    try:
        articles = await redis_client.get_articles()
        return articles
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@articles_router.get(
    "/{article_id}",
    response_model=dict,
    summary="Get article details",
    description="Retrieve details of a specific article"
)
async def get_article(article_id: str):
    """Get article details."""
    try:
        article = await redis_client.get_article(article_id)
        if not article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found"
            )
        return article
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@chat_router.post(
    "",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    summary="Process chat message",
    description="Process a chat message and return a response with session ID"
)
async def chat_endpoint(request: ChatRequest):
    """Process a chat message and return a response."""
    try:
        # Generate new session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())
        
        # Get response from RAG chain
        response_text = get_rag_answer(request.message)
        
        # Save message to history
        await redis_client.save_message(session_id, request.message, response_text)
        
        return {
            "session_id": session_id,
            "reply": response_text,
            "sources": []  # Add sources when implementing RAG
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@chat_router.get(
    "/{session_id}/history",
    response_model=ChatHistory,
    summary="Get chat history",
    description="Retrieve chat history for a session"
)
async def get_chat_history(session_id: str):
    """Get chat history for a session."""
    try:
        messages = await redis_client.get_chat_history(session_id)
        return {
            "session_id": session_id,
            "messages": messages
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

@chat_router.delete(
    "/{session_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete chat session",
    description="Delete a chat session and its history"
)
async def delete_session(session_id: str):
    """Delete a chat session."""
    success = await redis_client.delete_session(session_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    return None