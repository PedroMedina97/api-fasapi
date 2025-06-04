from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI(title= "MI API REST con FASTAPI")

class Item(BaseModel):
    id: Optional[UUID] = None
    nombre: str
    description: Optional[str] = None
    precio: float
    disponible: bool= True

items_db: List[Item] = []

@app.post("/items/", response_model=Item)
def crear_item(item: Item):
    item.id = uuid4()
    items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def obtener_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def obtener_item(item_id: UUID):
    for item in items_db:
        if item.id == item_id:
            return item
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
@app.put("/items/{item_id}", response_model=Item)
def actualizar_item(item_id: UUID, item_actualizado: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            item_actualizado.id = item.id
            items_db[idx] = item_actualizado
            return item_actualizado
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
@app.delete("/items/{item_id}")
def eliminar_item(item_id: UUID):
    for idx, item in enumerate(items_db):
        if item.id == item.id:
            del items_db[idx]
            return {"memsaje:" "Item eliminado"}
        raise HTTPException(status_code=404, detail="Item no encontrado")