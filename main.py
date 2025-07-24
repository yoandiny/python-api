from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post('/login')
def login(username: str, password: str):
    if(username == "admin" and password == "password"):
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}
    