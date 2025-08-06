from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name:str='Alok' # default value set as Alok
    age:Optional[int]=None
    
new_student={"age":45}
stude=Student(**new_student)
print(stude.name)
print(stude.age)