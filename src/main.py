from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.chat_client import ChatClient
from src.models.api_models import Input, Response, Result

app = FastAPI()


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: Response):
        super().__init__(status_code=status_code, detail=detail.model_dump())


@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(content=exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:

    response = Response(
        error=str(exc.errors()),
        result=None
    )

    return JSONResponse(content=response.model_dump(), status_code=400)


@app.get("/")
def root():
    return {"message": "Welcome to ChatGPT.MVP API."}


@app.get("/v1/status")
def health():
    return {"status": "OK"}


@app.post("/v1/chat")
def chat(input_data: Input) -> dict:

    try:

        # parse input
        message = input_data.message
        personality = input_data.personality

        bot = ChatClient()
        response = bot.chat(message=message, personality=personality)

        result = Result(answer=response)

        response = Response(
            error=None,
            result=result
        )

        return response.model_dump()

    except Exception as error:

        response = Response(
            error=str(error),
            result=None
        )

        raise CustomHTTPException(status_code=500, detail=response)

    pass
