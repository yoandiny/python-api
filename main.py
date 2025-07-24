from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()



@app.get("/hello")
def hello():
    return JSONResponse(content={"message": "Hello World"}, status_code=200)

@app.get('/welcome')
def welcome(name: str):
    return JSONResponse(content={"message": "Welcome "+ name}, status_code=200)

    
class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int


student_list = []

@app.post('/students')

def students(student: Student):
    
    student_list.append(student)
    
    return student_list
    

    

@app.get('/students')
def get_student():
    return student_list
