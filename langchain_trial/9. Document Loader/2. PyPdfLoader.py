# PyPDF Loader is a document loader in LangChain used to load content from PDF files and convert each page into a Document object.
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_vertexai import  ChatVertexAI
from dotenv import load_dotenv
load_dotenv()
loader=PyPDFLoader('9. Document Loader/Niteshwar.Resume.pdf')
docs=loader.load()
# print(docs[0])
prompt=PromptTemplate(
    template="Give me the a cover letter considering the job profile -> {job_profile} that i want to apply for from the text -> {text}. Also rate between 1-5",
    input_variables=['job_profile','text']
)
parser=StrOutputParser()
model=ChatVertexAI(model_name="gemini-2.5-pro")
chain=prompt|model|parser
res=chain.invoke({'job_profile':'Full-Stack Developer','text':docs[0].page_content})
print(res)