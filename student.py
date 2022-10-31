from fastapi import APIRouter
app = APIRouter()

student_list =[]

@app.post("/student")
async def add_student(student: dict) -> dict:
    student_list.append(student)
    return {"message": "Success"}

@app.get("/student")
async def get_student() -> dict:
    return {"student": student_list}