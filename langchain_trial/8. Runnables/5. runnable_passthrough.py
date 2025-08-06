from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel
# RunnablePassthrough -> gives the same input 
from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import ChatVertexAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# passthrough=RunnablePassthrough()
# print(passthrough.invoke({"name":"Alok"}))

prompt1=PromptTemplate(
    template="Write a joke about{topic}",
    input_variables=['topic']
)
model=ChatVertexAI(model_name="gemini-2.5-flash")
parser=StrOutputParser()

prompt2=PromptTemplate(
    template="Explain the following joke {text}",
    input_variables=['text']
)
joke_generator_chain=RunnableSequence(prompt1,model,parser)
paralell_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)
})
chain=RunnableSequence(joke_generator_chain,paralell_chain)
print(chain.invoke({'topic':'cricket'}))