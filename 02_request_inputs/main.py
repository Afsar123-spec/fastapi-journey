from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items/")
def read_item(name: str):
    return {"name": name}


@app.get("/products/")
def read_product(name: str, price: float = 0.0):
    return {"name": name, "price": price}

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name}, age {user.age}, created!"}
