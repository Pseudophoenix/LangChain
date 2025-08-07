from langchain_community.document_loaders import TextLoader
from langchain_google_vertexai import ChatVertexAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=ChatVertexAI(model_name="gemini-2.5-flash")
prompt=PromptTemplate(
    template="Write a summary for the following text - \n {text}",
    input_variables=['text']
)
parser=StrOutputParser()

loader=TextLoader('9. Document Loader\document_text.txt',encoding='utf-8')
doc=loader.load()
print(type(doc[0])) # a list of docs - <class 'langchain_core.documents.base.Document'>
# print(doc[0].page_content)
# print(doc[0].metadata)

chain=prompt|model|parser
res=chain.invoke({'text':doc[0].page_content})
print(res)