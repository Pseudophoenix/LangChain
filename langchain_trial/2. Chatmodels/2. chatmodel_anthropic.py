from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()
model=ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"))
res=model.invoke("What is the capital of India?")
print(res.content)
