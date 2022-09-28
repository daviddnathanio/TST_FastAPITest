from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI Test."}

@app.get("/{nim}")
async def nim_mahasiswa(nim: int):
    if nim < 10000000 or nim > 19999999:
        return {"message": "NIM tidak ada!"}
    else:
        return {"nim mahasiswa": nim}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/{nim}/{mahasiswa}")
async def show_mahasiswa(nim: int, mahasiswa: str):
    return {"nim": {nim}, "nama": {mahasiswa}}
    
