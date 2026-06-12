from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = ""

# In-memory storage
items = {}
next_id = 1

@app.get("/")
async def root():
    return {"message": "FastAPI starter app is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
async def list_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    global next_id
    item.id = next_id
    items[next_id] = item
    next_id += 1
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated.id = item_id
    items[item_id] = updated
    return updated

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Deleted"}
