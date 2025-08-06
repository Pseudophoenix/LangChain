# RunnableLambda-allows use to apply custom Python functions within an AI pipeline
# acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain Workflow.
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
def word_counter(text):
    return len(text.split())
# runnable_word_counter=RunnableLambda(word_counter)
# print(runnable_word_counter.invoke("Hi there how are you ?"))

prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
model=ChatVertexAI(model_name="gemini-2.5-flash")
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt|model|parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    # 'word_count':RunnableLambda(word_counter)
    "word_count":RunnableLambda(lambda x:len(x.split()))
})
final_chain=RunnableSequence(joke_gen_chain|parallel_chain)
result=final_chain.invoke({'topic':'AI'})
final_res="""
{}\n word count - {}""".format(result['joke'],result['word_count'])
print(final_res)
# print(res.joke)
# print(res.word_count)
