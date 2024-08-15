from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def insecure_function(data):
    eval(data)  # Dangerous use of eval()


@app.post("/execute")
async def execute_command(request: Request):
    # Dangerous use of subprocess with user input
    command = await request.body()
    subprocess.run(command, shell=True)


def get_user_data(username):
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query
