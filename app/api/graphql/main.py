from fastapi import APIRouter, Depends, Request
from fastapi.websockets import WebSocket
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from app.api.graphql.schema import schema
from app.api.dependencies.database import get_db

app = APIRouter()

# Custom context setup method
def get_context_value(request_or_ws: Request | WebSocket, _data) -> dict:
    return {
        "request": request_or_ws,
        "db": request_or_ws.scope["db"],
    }

# Create GraphQL App instance
graphql_app = GraphQL(
    schema,
    debug=True,
    context_value=get_context_value,
    websocket_handler=GraphQLTransportWSHandler(),
)

app.mount("/graphql/", graphql_app)


# Handle GET requests to serve GraphQL explorer
# Handle OPTIONS requests for CORS
@app.get("/graphql/")
@app.options("/graphql/")
async def handle_graphql_explorer(request: Request):
    return await graphql_app.handle_request(request)

# Handle POST requests to execute GraphQL queries
@app.post("/graphql/")
async def handle_graphql_query(
    request: Request,
    db = Depends(get_db),
):
    # Expose database connection to the GraphQL through request's scope
    request.scope["db"] = db
    return await graphql_app.handle_request(request)


# Handle GraphQL subscriptions over websocket
@app.websocket("/graphql")
async def graphql_subscriptions(
    websocket: WebSocket,
    db = Depends(get_db),
):
    # Expose database connection to the GraphQL through request's scope
    websocket.scope["db"] = db
    await graphql_app.handle_websocket(websocket)