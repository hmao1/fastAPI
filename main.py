from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#Mock data
class Student(BaseModel):
    name:str
    age: int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None

students={
    1:{"name": "cheng",
        "age": "20",
        "class": "year 12"
    },
    2:{"name": "Ben",
        "age": "20",
        "class": "year 12"
    },
    3:{"name": "zhe",
        "age": "20",
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name" : "Hello World!"}

@app.get("/get-student/{student_id}")
async def get_student(student_id:int):
    return students[student_id]

@app.get("/get-student-by-name")
def get_student(name:str):
    for student_id in students:
        if(students[student_id]["name"] == name):
            return students[student_id]
    return {"data": "Not Found"}  

@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error": "student id already exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if(student_id in students):
        for key, value in student:
            if(value):
                students[student_id][key] = value
        return students[student_id]
    return  {"error": "student id does not exist!"}  
