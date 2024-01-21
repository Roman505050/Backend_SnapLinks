from urllib.request import Request
from fastapi import FastAPI, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": jsonable_encoder(exc.errors(), exclude={"url", "input"})})


main_router = APIRouter(prefix="/api")