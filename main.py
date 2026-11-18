from langchain.chat_models import init_chat_model
from langgraph.graph import START, END, MessagesState, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from nodes import chat_node

load_dotenv()

llm = init_chat_model(model = 'openai:gpt-4o')


builder = StateGraph(MessagesState)
builder.add_node('chat_node', chat_node)


builder.add_edge(START, 'chat_node')
builder.add_edge('chat_node', END)

graph = builder.compile(checkpointer=InMemorySaver())