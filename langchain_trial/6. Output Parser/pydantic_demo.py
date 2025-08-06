from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name:str='Alok' # default value set as Alok
    age:Optional[int]=None # Optional value
    
new_student={"age":"45"} # Coercing - string converted implicitly into int by pydantic
stude=Student(**new_student)
print(stude.name)
print(type(stude.age))