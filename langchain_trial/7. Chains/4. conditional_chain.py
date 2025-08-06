from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
# RunnableBranch for conditional branching
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()
model1=ChatVertexAI(model_name="gemini-2.5-pro")
parser=StrOutputParser()
class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")
parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative\n{feedback}\n{format_instruction}",
    input_variables=['feedback'],
    partial_variables={
        'format_instruction':parser2.get_format_instructions()
    }
)
classifier_chain=prompt1|model1|parser2
prompt2=PromptTemplate(
    template="Write an appropriate response to this positive feedback\n{feedback}",
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template="Write an appropriate response to this negative feedback\n{feedback}",
    input_variables=['feedback']
)
# branch_chain=RunnableBranch(
#     (condition1,chain1),
#     (condition2,chain2)
#       default chain
# )
# res=classifier_chain.invoke({"feedback":"This is a wonderful smartphone"})
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt2|model1|parser),
    (lambda x:x.sentiment=="negative",prompt3|model1|parser),
    RunnableLambda(lambda x:"Could not find sentiment")
    # default chain
)
final_chain=classifier_chain|branch_chain
final_res=final_chain.invoke({"feedback":"This is a terrible phone"})
print(final_res)
final_chain.get_graph().print_ascii()
