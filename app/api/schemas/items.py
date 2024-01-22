from pydantic import BaseModel

# Schema for creating a new item
class ItemCreate(BaseModel):
    name: str
    description: str

# Schema for the response of an item (including its ID)
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True

# Schema for updating an item
class ItemUpdate(BaseModel):
    name: str
    description: str
