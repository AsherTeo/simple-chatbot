from main import graph
from uuid import uuid4

config = {'configurable': {'thread_id': str(uuid4())}}

while True:
    question = input("User: ")
    if question == 'exit':
        break 

    result = graph.invoke({'messages': [{'role': 'user', 'content': question}]}, config)

    print(result['messages'][-1].content)