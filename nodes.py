from langgraph.graph import MessagesState
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model = 'openai:gpt-4o')

def chat_node(state: MessagesState):
    input = state['messages']
    response = llm.invoke(input)

    return {'messages': [response]}