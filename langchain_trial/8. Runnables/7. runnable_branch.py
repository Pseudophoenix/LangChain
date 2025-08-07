# a control flow component in LangChain that allows us to conditionally route input data to different chains or runnables based on custom logic
# It functions like an if/elif/else block for chains - where we define a set of condition functions, each associated with a runnable(e.g LLM call, prompt chain, or tool). The first matching condition is executed. If no conition matches, a default runnable is used (if provided).
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda
load_dotenv()

prompt=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Summarize the following text\n{text}",
    input_variables=['text']
)
model=ChatVertexAI(model_name="gemini-2.5-flash")
parser=StrOutputParser()
report_gen_chain=RunnableSequence(prompt,model,parser)
branch_chain=RunnableBranch(
    # (condition,runnable),
    (lambda x:len(x.split())>200,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)
final_chain=RunnableSequence(report_gen_chain,branch_chain)
res=final_chain.invoke({'topic':'Russia Ukraine War'})
print(res)
