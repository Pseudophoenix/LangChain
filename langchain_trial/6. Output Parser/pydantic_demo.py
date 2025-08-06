from pydantic import BaseModel
class Student(BaseModel):
    name:str
new_student={'name':45}
stude=Student(**new_student)
print(type(stude))