# News Chatbot with RAG

A full-stack chatbot application that answers queries using a Retrieval-Augmented Generation (RAG) pipeline over a news corpus.

## Features

- **RAG Pipeline**: Ingest news articles, generate embeddings, and retrieve relevant context
- **Session Management**: Each user gets a unique session with chat history
- **Persistent Storage**: Redis for session management and chat history
- **Modern UI**: Built with React and Tailwind CSS

## Tech Stack

- **Backend**: FastAPI (Python 3.11+)
- **Frontend**: React + Vite + Tailwind CSS
- **Vector Database**: ChromaDB
- **Embeddings**: Jina AI
- **LLM**: Google Gemini
- **Caching & Sessions**: Redis

## Prerequisites

- Python 3.11+
- Node.js 18+
- Redis
- Google Gemini API Key
- Jina AI API Key

## Demo
![image](https://github.com/user-attachments/assets/4fdeb665-0b3b-4aa0-aba6-c797b00b83a1)

![image](https://github.com/user-attachments/assets/13f6bfa9-939e-4eff-a12e-48e619860c99)

![image](https://github.com/user-attachments/assets/3ebf96a0-4ea6-4cfc-9c05-a3c2e97ed591)

## Setup

### Backend

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your API keys

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file with:
   ```
   VITE_API_URL=http://localhost:8000
   ```

## Running the Application

### Start Redis

Make sure Redis is running locally or update the Redis configuration in `.env`.

### Start Backend

```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Start Frontend

```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:5173`

## API Endpoints

- `POST /api/chat` - Send a chat message
- `GET /api/chat/{session_id}` - Get chat history for a session
- `DELETE /api/chat/{session_id}` - Delete a chat session

## Configuration

### Redis TTL

Session data in Redis is set to expire after 24 hours by default. You can adjust this in `app/db/redis_client.py` by modifying the `ttl` attribute in the `RedisManager` class.

### Caching

- **Chat History**: Stored in Redis with TTL
- **Embeddings**: Cached in ChromaDB


## Deployment

### Backend

1. Set `ENVIRONMENT=production` in `.env`
2. Use a production ASGI server like Uvicorn with Gunicorn:
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
   ```

### Frontend

Build for production:

```bash
cd frontend
npm run build
```

## License

MIT
