from http import HTTPStatus
from starlette.responses import Response
from fastapi import FastAPI, APIRouter
from schemas import *
import json

app = FastAPI()

# Router
router = APIRouter()
router.include_router(router, prefix="/events", tags=["events"])

@router.post("/", dependencies=[])
def handle_event(data: EventSchema) -> Response:
    print(data)
    return Response(
        content=json.dumps({"message": "Data received!"}),
        status_code=HTTPStatus.ACCEPTED,
    )

app.include_router(router)
