from unittest.mock import MagicMock, patch
from nodes import llm
from langchain.messages import AIMessage
import nodes 
from main import graph 
from uuid import uuid4 
import api as api_module
from fastapi.testclient import TestClient

def test_graph():

    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content='Today is Friday!!!!')

    with patch.object(nodes, 'llm', fake_llm):
        config = {'configurable': {'thread_id': uuid4()}}

        response = graph.invoke({'messages': [{'role': 'user', 'content': 'What day is today?'}]}, config)

        assert response['messages'][-1].content == fake_llm.invoke.return_value.content


def test_end_point():
    client = TestClient(api_module.api) 

    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content="Today is Sunny!!!!")

    with patch.object(nodes, "llm", fake_llm):
        response = client.post("/chat", json={"q": "What weather is today?"})

    assert response.status_code == 200
    assert response.json() == {"AI": "Today is Sunny!!!!"}


        