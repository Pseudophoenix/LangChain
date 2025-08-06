from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence
load_dotenv()

prompt1=PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=['topic']
)
model=ChatVertexAI(model_name="gemini-2.5-flash")
parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkedin':RunnableSequence(prompt2,model,parser)
    }
)
result=parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print("\n\n")
print(result['linkedin'])