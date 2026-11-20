from fastapi import FastAPI 
from main import graph
import uvicorn
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Literal, Optional

class Query(BaseModel):
    q : str 


api = FastAPI()

@api.get('/home')
def home():
    return 'Fastapi is working'

@api.post('/chat')
def chat(prompt: Query):
    query = prompt.q
    config = {'configurable': {'thread_id': uuid4()}}
    response = graph.invoke({'messages': [{'role': 'user', 'content': query}]}, config)
    return {"AI": response['messages'][-1].content }

if __name__ == "__main__":
    uvicorn.run(api, host= "0.0.0.0", port= 8000, reload=True)