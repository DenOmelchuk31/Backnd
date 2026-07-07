from fastapi import FastAPI
from pydantic import BaseModel
from starlette.status import HTTP_200_OK

app = FastAPI()

class Health(BaseModel):
    status_code: int
    detail: str
    result: str


@app.get("/", status_code=HTTP_200_OK)
def health_check():
    return Health(
        status_code=HTTP_200_OK,
        detail="ok",
        result="working"
    )