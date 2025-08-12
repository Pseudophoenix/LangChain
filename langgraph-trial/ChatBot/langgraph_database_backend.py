from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_core.messages  import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
llm=ChatVertexAI(model_name="gemini-2.5-pro")


class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def chat_node(state:ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {"messages":[response]}

checkpointer=InMemorySaver()
graph=StateGraph(ChatState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot=graph.compile(checkpointer=checkpointer)