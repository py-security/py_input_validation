from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise RuntimeError("API_KEY nicht gesetzt!")

app = FastAPI()

class Item(BaseModel):
    name: str  = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)

@app.get("/")
def read_root():
    return {"message": "Sichere API laeuft"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item-ID muss positiv sein")
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item, api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Nicht autorisiert")
    return {"item": item.dict()}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )