from unittest.mock import MagicMock, patch
from langchain.messages import AIMessage 
import main, nodes

def test_system():
    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content="This is a testing bot")

    with patch.object(nodes, 'llm', fake_llm):
        result = nodes.chat_node({"messages":[{'role': 'user', 'content': 'what bot is this ?'}]})

    assert result['messages'][-1].content == fake_llm.invoke.return_value.content


def test_pipeline():
    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content="today is sunny day")

    with patch.object(nodes, "llm", fake_llm):
        config = {"configurable": {"thread_id": "t1"}}
        response = main.graph.invoke(
            {"messages": [{"role": "user", "content": "what weather is it now ?"}]},
            config,
        )

    assert response["messages"][-1].content == "today is sunny day"
    