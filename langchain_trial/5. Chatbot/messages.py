from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
load_dotenv()
model=Ollama(model=os.getenv("OLLAMA_MODEL"))
messages=[
    SystemMessage(content="You are a helpful gardener"),
    HumanMessage(content="Tell me about GrassHoppers"),
    
]
res=model.invoke(messages)
messages.append(AIMessage(content=res))
print(messages)
