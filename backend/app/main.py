from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import chat_router, articles_router
import os

def create_app() -> FastAPI:
    app = FastAPI(
        title="News Chatbot API",
        description="Simple RAG-based news chatbot with session management",
        version="1.0.0",
        docs_url="/docs"
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    # Include API routes
    app.include_router(chat_router)
    app.include_router(articles_router)
    
    # Create cleaned_articles directory if it doesn't exist
    os.makedirs('cleaned_articles', exist_ok=True)
    
    @app.get("/api/health")
    def health_check():
        return {"status": "healthy"}
    
    return app

# Create app instance for uvicorn
app = create_app()