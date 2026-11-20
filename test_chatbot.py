from unittest.mock import MagicMock, patch
from nodes import llm
from langchain.messages import AIMessage
import nodes 
from main import graph 
from uuid import uuid4 

def test_pipeline():

    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content='Today is Friday!!!!')

    with patch.object(nodes, 'llm', fake_llm):
        config = {'configurable': {'thread_id': uuid4()}}

        response = graph.invoke({'messages': [{'role': 'user', 'content': 'What day is today?'}]}, config)

        assert response['messages'][-1].content == fake_llm.return_value.content