from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()
# chat_history=[]
chat_history=[
    SystemMessage(content="You are a car specialist"),
    
]
model = Ollama(model=os.getenv("OLLAMA_MODEL"))
while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print(f"AI: {result}")
    
# Context storing ability that is ability to remember past aka chat history
# Three types of message in langchain
# 1. System Message
# 2. Humarn Message
# 3. AI Message