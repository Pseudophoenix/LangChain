from langchain_community.document_loaders import TextLoader
loader=TextLoader('9. Document Loader\document_text.txt',encoding='utf-8')
doc=loader.load()
print(type(doc[0])) # a list of docs - <class 'langchain_core.documents.base.Document'>