from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
# llm=HuggingFaceEndpoint(
#     repo_id="",
#     task="text-generation"
# )
# model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()
# To use model
model = VertexAI(model_name="gemini-2.5-pro")
# res=model.invoke("Where is Paris and what is it famouse for recently?")
template=PromptTemplate(
    template="Give me the 5 facts about {topic}\n {format_instruction}",
    # template="Give me the name, age, and city of a fictional person\n {format_instruction}",
    input_variables=['topic'],
    # 
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.format()
# res=model.invoke(prompt)
# print(prompt)
# final_res=parser.parse(res)
chain=template|model|parser
final_res=chain.invoke({'topic':"baldness in India"})
print(final_res)
# print(final_res['name'])
print(type(final_res))