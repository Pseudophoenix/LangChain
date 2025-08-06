# from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
# model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
# res=model.invoke("What is the capital of India?")
# print(res.content)

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="give the lyrics of sun raha hai na tu ro raha hu main",
)

print(response.text)