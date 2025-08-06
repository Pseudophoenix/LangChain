# documents=[
    
# ]
# query=""
# doc_embeddings=embedding.embed_documents(documents)
# query_embedding=embedding.embed_query(query)

# scores=cosine_similarity([query_embedding],doc_embeddings)[0]
# index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] # Sort using second value as the key
# print(documents[index])
# print("Similarity Score: ",score)

# from langchain_huggingface import ChatHuggingFace
# from transformers import pipeline
# from langchain_huggingface import HuggingFacePipeline
# import torch
# pipe = pipeline("text-generation", 
#                model="sentence-transformers/all-MiniLM-L6-v2", 
#                torch_dtype=torch.bfloat16, 
#                device_map="auto")

# llm = HuggingFacePipeline(pipeline=pipe)
# model = ChatHuggingFace(llm=llm)
# res = model.invoke("What is capital of Russia?")
# print(res.content)


# from langchain_community.embeddings import HuggingFaceEmbeddings

# # Initialize the embedding model
# embed_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Generate embeddings for text
# text = "What is the capital of Russia?"
# embeddings = embed_model.embed_query(text)
# print(embeddings[:5])  # Show first 5 dimensions of the vector

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Encode sentences
sentences = ["What is the capital of Russia?"]
embeddings = model.encode(sentences)

print(embeddings.shape)  # (1, 384) - 1 vector of 384 dimensions
print(embeddings[0][:5])  # First 5 dimensions