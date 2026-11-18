from unittest.mock import MagicMock, patch
from langchain.messages import AIMessage 
import nodes

def test_system():
    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content="This is a testing bot")

    with patch.object(nodes, 'llm', fake_llm):
        result = nodes.chat_node({"messages":[{'role': 'user', 'content': 'what bot is this ?'}]})

    assert result['messages'][-1].content == fake_llm.invoke.return_value.content