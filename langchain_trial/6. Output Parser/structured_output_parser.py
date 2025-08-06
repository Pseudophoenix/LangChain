from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain_google_vertexai import VertexAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()
model = VertexAI(model_name="gemini-2.5-pro")
schema=[
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    
    ResponseSchema(name='fact_3',description='Fact 3 about the topic'),
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give 3 facts about{topic}\n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)
# prompt=template.invoke({'topic':"fall of ground water level"})
# result=model.invoke(prompt)
# final_res=parser.parse(result)
chain=template|model|parser
final_res=chain.invoke({'topic':"cosmic rays"})
print(final_res)