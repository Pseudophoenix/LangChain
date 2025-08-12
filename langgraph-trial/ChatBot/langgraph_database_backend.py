from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_core.messages  import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3 
load_dotenv()
llm=ChatVertexAI(model_name="gemini-2.5-pro")
conn=sqlite3.connect(database="chatbot.db",check_same_thread=False)

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def chat_node(state:ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {"messages":[response]}

# checkpointer=InMemorySaver()
checkpointer=SqliteSaver(conn=conn)
graph=StateGraph(ChatState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot=graph.compile(checkpointer=checkpointer)

# response=chatbot.invoke({
#     'messages':[HumanMessage(content="What is my capital of USA")]
# },config={"configurable":{"thread_id":"2"}})

# print(response)