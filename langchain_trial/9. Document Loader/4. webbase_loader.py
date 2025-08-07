from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()
model=ChatVertexAI(model_name="gemini-2.5-flash")
prompt=PromptTemplate(
    template="Write a short summary for the device mentioned in the text - \n {text}",
    input_variables=['text']
)
parser=StrOutputParser()

url="https://www.xfinity.com/mobile/shop/phone/galaxy-z-fold7?colorName=Blue%20Shadow"
loader=WebBaseLoader(url)
# docs=loader.lazy_load()
docs=loader.load()
for doc in docs:
    # print(len(docs))
    print(doc.page_content)
# chain = prompt|model|parser
# res=chain.invoke({'text':docs[0].page_content})
# print(res)
