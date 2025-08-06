# from langchain_huggingface import HuggingFaceEndpoint
# from langchain.chains import LLMChain
# from langchain_core.prompts import PromptTemplate
# from getpass import getpass

# HUGGINGFACEHUB_API_TOKEN = getpass()
# import os

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
# question = "Who won the FIFA World Cup in the year 1994? "

# template = """Question: {question}

# # Answer: Let's think step by step."""

# prompt = PromptTemplate.from_template(template)
# # print(prompt)
# repo_id = ""

# # llm = HuggingFaceEndpoint(
# #     repo_id=repo_id,
# #     # max_length=128,
# #     temperature=0.5,
# #     huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
# #     provider="auto",  # set your provider here hf.co/settings/inference-providers
# #     # provider="hyperbolic",
# #     # provider="nebius",
# #     # provider="together",
# # )

# llm=HuggingFaceEndpoint(repo_id="arcee-ai/AFM-4.5B",
#                         task="text-generation")
# model=ChatHuggingFace(llm=llm)
# res=model.invoke("Where is Paris and what is it famous for?")
# # llm_chain = prompt | llm
# # print(llm_chain.invoke({"question": question}))
# print(res)