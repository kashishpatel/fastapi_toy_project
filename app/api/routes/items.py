from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.items import ItemCreate, ItemResponse
from ..crud.items import create_item, get_items, get_item, update_item, delete_item
from ..dependencies.database import get_db
from app.utils.jwt_auth import verify_jwt_token

router = APIRouter()

# Create an item
@router.post("/items/", response_model=ItemResponse)
async def create_new_item(item: ItemCreate, current_user: str = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    return create_item(db, item)

# Get a list of all items
@router.get("/items/", response_model=list[ItemResponse])
async def list_items(current_user: str = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    return get_items(db)

# Get a single item by ID
@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_single_item(item_id: int, current_user: str = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Update an item by ID
@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_existing_item(item_id: int, item: ItemCreate, current_user: str = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    existing_item = get_item(db, item_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_item(db, item_id, item)

# Delete an item by ID
@router.delete("/items/{item_id}", response_model=ItemResponse)
async def delete_item_by_id(item_id: int, current_user: str = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    existing_item = get_item(db, item_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return delete_item(db, item_id)
