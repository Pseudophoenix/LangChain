from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
from langchain_community.llms import Ollama
# from langchain_openai import OpenAI
import os
from langchain_core.prompts import PromptTemplate,load_prompt
model = Ollama(model=os.getenv("OLLAMA_MODEL"))
# model=ChatOpenAI(model=os.getenv("OPENAI_MODEL"),temperature=1.9)
# ,max_completion_tokens=20)
# response = model.invoke("Give an essay on taj mahal")

paper_input=st.selectbox("Search Research Paper Name",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox("Select Explaination Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])
length_input=st.selectbox("Select Explaination Length",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explaination)"])

# we could have used a f string in place of PromptTemplate but PromptTemplates comewith some validation 
template=load_prompt('template.json')
# template=PromptTemplate(
#             template="""
#             Please summarize the research paper titled "{paper_input}" with the following specifications:
#             Explaination Style:{style_input}
#             Explaination Lenght:{length_input}
#             1. Mathematical Details:
#                 - include relevant mathematical equations if present in the paper.
#                 - explain the mathematical concepts using simple, intuitive code snippets where applicable!
#             2. Analogies:
#                 - use relatable analogies to simplify complex ideas.
#             If certain information is not available in the paper, respond with "Insufficient Information available" instead of guessing. 
#             Ensure the summary is clear, accurate and aligned with the provided style and length
#             """,
#             input_variable=["paper_input","style_input","length_input"]
# )
# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })
# header
st.header("Research Tool")
# user_input=st.text_input("Enter your prompt")
if st.button('Summarize'):
    chain=template|model
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })
    # st.text("Some random text")
    
    # result=model.invoke(user_input)
    # result=model.invoke(prompt)
    # st.text(user_input)
    st.write(result)