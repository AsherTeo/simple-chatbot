
# Chatbot

A LangGraph chatbot served with FastAPI and packaged with Docker.

## Features
- LangGraph workflow with memory
- FastAPI `/chat` endpoint
- Dockerized
- Tests with pytest, CI with GitHub Actions

## Run locally
```bash
pip install -r requirements.txt
uvicorn api:api --port 8000
```

## Run with Docker
```bash
docker build -t chatbot .
docker run -d -p 8000:8000 --env-file .env --name chatbot chatbot
```

## Usage
Open `http://localhost:8000/docs`, or:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"q": "hello"}'
```

## Tests
```bash
pytest -v
```