from fastapi import HTTPException
from ariadne import gql, QueryType, MutationType, make_executable_schema
from app.api.schemas.items import ItemCreate
from app.api.crud.items import create_item, get_items, get_item, update_item, delete_item

type_defs = gql("""
    type Item {
        id: Int!
        name: String!
        description: String
    }

    input ItemInput {
        name: String!
        description: String
    }

    type Query {
        items: [Item!]!
        item(id: Int!): Item
    }

    type Mutation {
        createItem(input: ItemInput!): Item!
        updateItem(id: Int!, input: ItemInput!): Item!
        deleteItem(id: Int!): Item!
    }
""")

query = QueryType()
mutation = MutationType()

@query.field("items")
def resolve_items(_, info):
    try:
        db = info.context["db"]
        items = get_items(db)
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@query.field("item")
def resolve_item(_, info, id):
    try:
        db = info.context["db"]
        item = get_item(db, id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@mutation.field("createItem")
def resolve_create_item(_, info, input):
    try:
        db = info.context["db"]
        item = ItemCreate(name=input['name'], description=input['description'])
        new_item = create_item(db, item)
        return new_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@mutation.field("updateItem")
def resolve_update_item(_, info, id, input):
    try:
        db = info.context["db"]
        item = ItemCreate(name=input['name'], description=input['description'])
        updated_item = update_item(db, id, item)
        if not updated_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@mutation.field("deleteItem")
def resolve_delete_item(_, info, id):
    try:
        db = info.context["db"]
        deleted_item = delete_item(db, id)
        if not deleted_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return deleted_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

schema = make_executable_schema(type_defs, query, mutation)