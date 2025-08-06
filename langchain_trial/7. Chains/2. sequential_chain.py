from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt1=PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate a 5 pointer summary from the following text\n{text}",
    input_variables=['text']
)
model=ChatVertexAI(model_name="gemini-2.5-flash")
parser=StrOutputParser()
chain=prompt1|model|parser|prompt2|model|parser
res=chain.invoke({"topic":"Pollution of air due to CFCs"})
print(res)
chain.get_graph().print_ascii()