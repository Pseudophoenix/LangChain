from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import ChatVertexAI
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path="books",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()
# print(len(docs))
print(docs[1320].page_content)
print(docs[1320].metadata)