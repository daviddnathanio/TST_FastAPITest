from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI Test."}

# Bikin class, isinya bebas.
class student(BaseModel):
    nim: int
    nama: str

# Bikin Array buat menampung class tadi. Nanti fungsi POST akan meng-append arraynya.
student_list = []


@app.post("/student")
async def add_student(model: student): #Bikin variabel parameter baru yang JENISNYA adalah CLASS YANG UDAH DIBUAT TADI.
    student_list.append(model)
    return {"message": "Success"}

@app.get("/student")
async def get_student():
    return {"student": student_list}


