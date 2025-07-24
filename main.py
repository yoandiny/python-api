from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class User(BaseModel):
    username: str
    password: str


@app.post('/login')
def login(user: User):
    if(user.username == "admin" and user.password == "password"):
        return JSONResponse(content={"message": "Login successful"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Login failed"}, status_code=401)
    