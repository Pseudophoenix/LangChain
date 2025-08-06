from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name:str='Alok' # default value set as Alok
    age:Optional[int]=None # Optional value
    email:Optional[EmailStr]='abc@gmail.com'
    cgpa:float=Field(gt=0,lt=10,default=5,description="Decimal value representing the CGPA of the student")
new_student={
    "age":"45","email":"abc@gmail.com"
            #  ,"cgpa":9
} # Coercing - string converted implicitly into int by pydantic
# EmailStr is a builtin class provided for validation of Email address
# FieldFunction -> default values, constraints, RegEx
stude=Student(**new_student)
stude_json=stude.model_dump_json()
stude_dict=dict(stude)
print(stude_dict)
print(stude_json)
print(stude)