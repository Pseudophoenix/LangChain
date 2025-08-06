# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
# llm=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                        # task="text-generation")
# model=ChatHuggingFace(llm=llm)
# model = Ollama(model=os.getenv("OLLAMA_MODEL"))
# response = model.invoke("Give an essay on taj mahal")

# from google import genai

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)
model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# 1st prompt -> detailed report

template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)
# 2nd prompt -> summary
template2=PromptTemplate(
    template="Write a five line summary on the following text.\n {text}",
    input_variables=['text']
)
# prompt1=template1.invoke({'topic':'black hole'})
# res=model.invoke(prompt1)
# print(res)
# prompt2=template2.invoke({'text':res})
# summary=model.invoke(prompt2)
# print("\n\n")
# print(summary)
parser=StrOutputParser()
chain=template1|model|parser|template2|model|parser
result=chain.invoke({"topic":"Black hole"})
print(result)