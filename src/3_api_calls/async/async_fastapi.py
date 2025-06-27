"""
FastAPI

Key Concepts:
1. Server side only
2. Fast, modern async framework for building APIs in python
3. Fast based on (starlette and Pydantic), easy to use
"""

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

import uvicorn

app= FastAPI()


# Landing page
@app.get("/")
async def landing_page():
    return "HELLO WORLD"


# post request, sender hand to send a json body
@app.post("/echo")
async def echo(request: Request):
    """
    using curl:

    curl -X POST http://localhost:8000/echo \
         -H "Content-Type: application/json" \
         -d '{"hello": "world"}'
    """
    data = await request.json()
    return data


# Request body with pydantic models
class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


# Error Handling
@app.get("/fail/{x}")
async def fail(x: int):
    if x < 0:
        raise HTTPException(status_code=400, detail="x must be > 0")
    return {"x": x}


# running fast api locally
if __name__ == "__main__":
    uvicorn.run("async_fastapi:app", host="127.0.0.1", port=8000, reload=True)
