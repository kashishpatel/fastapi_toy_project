from sqlalchemy.orm import Session
from app.db import models  # Import your SQLAlchemy models from the database module
from ..schemas.items import ItemCreate, ItemResponse

# Create a new item in the database
def create_item(db: Session, item: ItemCreate) -> ItemResponse:
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get a list of all items from the database
def get_items(db: Session) -> list[ItemResponse]:
    items = db.query(models.Item).all()
    return items

# Get a single item by ID from the database
def get_item(db: Session, item_id: int) -> ItemResponse:
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

# Update an existing item in the database
def update_item(db: Session, item_id: int, item: ItemCreate) -> ItemResponse:
    existing_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if existing_item:
        for key, value in item.dict().items():
            setattr(existing_item, key, value)
        db.commit()
        db.refresh(existing_item)
    return existing_item

# Delete an item by ID from the database
def delete_item(db: Session, item_id: int) -> ItemResponse:
    existing_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if existing_item:
        db.delete(existing_item)
        db.commit()
    return existing_item
