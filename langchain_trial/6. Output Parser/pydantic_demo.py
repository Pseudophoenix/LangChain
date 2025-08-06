from pydantic import BaseModel
class Student(BaseModel):
    name:str='Alok'
new_student={}
stude=Student(**new_student)
print(stude)