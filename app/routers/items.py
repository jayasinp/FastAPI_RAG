from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import SessionLocal, mongo_db
from ..models import Item

router = APIRouter()

# Pydantic model for request body
class ItemCreate(BaseModel):
    name: str
    description: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/")
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    # Insert into MongoDB
    await mongo_db.items.insert_one({"name": item.name, "description": item.description})

    return db_item

@router.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item
