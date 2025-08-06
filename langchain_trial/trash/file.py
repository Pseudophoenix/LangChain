# from langchain_community.llms import Ollama
# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# import os
# load_dotenv()
# model = Ollama(model=os.getenv("MODEL_NAME"))
# response = model.invoke("Give an essay on taj mahal")

# print(response)

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the OpenAI model
model = OpenAI(model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo-instruct"))  # Default to gpt-3.5-turbo-instruct if not specified

# Get response from the model
response = model.invoke("Give an essay on Statue of Liberty")

# Print the response
print(response)


# from openai import OpenAI

# client = OpenAI(
#   api_key=""
# )

# response = client.responses.create(
#   model="gpt-4o-mini",
#   input="write a essay on eiffle tower",
#   store=True,
# )

# print(response.output_text);


# # from openai import OpenAI
# # from dotenv import load_dotenv
# # import os
# # # load_dotenv()
# # # openai_client = OpenAI(api_key="")
# # # This is the retriever we will use in RAG
# # # This is mocked out, but it could be anything we want
# # # def retriever(query: str):
# # #     results = ["Harrison worked at Kensho"]
# # #     return results

# # # # This is the end-to-end RAG chain.
# # # # It does a retrieval step then calls OpenAI
# # # def rag(question):
# # #     docs = retriever(question)
# # #     system_message = """Answer the users question using only the provided information below:
    
# # #     {docs}""".format(docs="\n".join(docs))
    
# # #     return openai_client.chat.completions.create(
# # #         messages=[
# # #             {"role": "system", "content": system_message},
# # #             {"role": "user", "content": question},
# # #         ],
# # #         model="gpt-4o-mini",
# # #     )
# # # rag("where did harrison work")


# # from openai import OpenAI
# # from langsmith.wrappers import wrap_openai

# # openai_client = wrap_openai(OpenAI(api_key=""))

# # # This is the retriever we will use in RAG
# # # This is mocked out, but it could be anything we want
# # def retriever(query: str):
# #     results = ["Harrison worked at Kensho"]
# #     return results

# # # This is the end-to-end RAG chain.
# # # It does a retrieval step then calls OpenAI
# # def rag(question):
# #     docs = retriever(question)
# #     system_message = """Answer the users question using only the provided information below:
    
# #     {docs}""".format(docs="\n".join(docs))
    
# #     return openai_client.chat.completions.create(
# #         messages=[
# #             {"role": "system", "content": system_message},
# #             {"role": "user", "content": question},
# #         ],
# #         model="gpt-4o-mini",
# #     )
# # rag("where did harrison work")