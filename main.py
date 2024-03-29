#pip install fastapi uvicorn
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  dummy_data = {"word": "Hello world"}
  return dummy_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
  
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

#python 3.6x
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
