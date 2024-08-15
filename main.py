from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

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


def get_user_data(username):
    print(username)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Vulnerable to SQL injection
    cursor.execute(query)
    return cursor.fetchall()
