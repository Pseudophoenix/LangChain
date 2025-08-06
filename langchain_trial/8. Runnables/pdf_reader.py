from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
loader=TextLoader('docs.txt')
documents=loader.load()
# Split the text into smaller chunks
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=text_splitter.split_documents(documents)
# Convert text into embeddings & store in FAISS
vectorstore=FAISS.from_documents(docs,OpenAIEmbeddings())
retriever=vectorstore.as_retriever()
query="What are the key takeaways from the document?"
retrieved_docs=retriever.get_relevant_documents(query)
retrieved_text="\n".join({doc.page_content for doc in retrieved_docs})
llm=OpenAI(model_name="gpt-3.5-turbo",temperature=0.7)