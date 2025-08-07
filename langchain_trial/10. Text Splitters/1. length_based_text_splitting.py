from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('books\C++ - The Complete Reference - Herbert Schildt (4th ed.).pdf')
# text="""
# The National Democratic Alliance (NDA) is set to announce its Vice Presidential candidate on August 12, with the final decision to be made by Prime Minister Narendra Modi and BJP President JP Nadda. This development follows the resignation of Vice President Jagdeep Dhankhar due to health reasons on the first day of the Monsoon Session, a move that has drawn skepticism from the Opposition. An NDA meeting was held to discuss the nominee and strategize for the election, including training MPs to prevent invalid votes.
# """
 
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0, # 
    separator=""
)
docs=loader.load()
res=splitter.split_documents(docs)
print(res[100].page_content)
# for doc in res:
#     print(doc.page_content)
# docs=loader.lazy_load()
# for doc in docs:
#     res=splitter.split_text(doc.page_content)
#     print(res)