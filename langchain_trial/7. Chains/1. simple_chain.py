from langchain_google_vertexai import VertexAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt=PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)
model=VertexAI(model_name="gemini-2.5-pro")
parser=StrOutputParser()
chain=prompt|model|parser

chain.invoke({'topic':"Nile River egypt"})