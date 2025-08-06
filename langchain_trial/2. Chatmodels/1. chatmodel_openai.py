from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
model=ChatOpenAI(model=os.getenv("OPENAI_MODEL"),temperature=1.9,max_completion_tokens=20)
result=model.invoke("Suggest me 5 indian kid names?")
print(result.content)
