from typing import TypedDict
from langchain_google_vertexai import VertexAI
model=VertexAI(model_name="gemini-1.5-pro")
class Person(TypedDict):
    name:str
    age:int
new_person:Person={
    "name":"Alok",
    "age":41
}