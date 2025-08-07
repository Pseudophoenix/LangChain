from langchain_community.document_loaders import CSVLoader 
loader=CSVLoader(file_path="")
data=loader.load()
print(data[0].page_content)
# We can even create our custom DATALOADERS
