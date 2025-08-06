from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_google_vertexai import VertexAI
load_dotenv()
model = VertexAI(model_name="gemini-2.5-pro")
class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="Name of the city the person belongs to")
parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template="Generate the name, age and city of a fictional {place} girl\n{format_instructions}",
    input_variables=['place'],
    partial_variables={
        'format_instructions':parser.get_format_instructions()
    }
)
# prompt=template.invoke({"place":"Indian"})
# print(prompt)
# res=model.invoke(prompt)
chain=template|model|parser
# final_res=parser.parse(res)
final_res=chain.invoke({'place':"indian"})
print(final_res)