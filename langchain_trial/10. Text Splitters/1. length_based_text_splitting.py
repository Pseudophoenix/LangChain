from langchain.text_splitter import CharacterTextSplitter
text="""
The National Democratic Alliance (NDA) is set to announce its Vice Presidential candidate on August 12, with the final decision to be made by Prime Minister Narendra Modi and BJP President JP Nadda. This development follows the resignation of Vice President Jagdeep Dhankhar due to health reasons on the first day of the Monsoon Session, a move that has drawn skepticism from the Opposition. An NDA meeting was held to discuss the nominee and strategize for the election, including training MPs to prevent invalid votes.
"""
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)
res=splitter.split_text(text)
print(res)