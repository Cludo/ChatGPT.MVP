from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.chat_client import ChatClient
from src.models.api_models import Input, Response, Result

# create a FastAPI instance
app = FastAPI()


class CustomHTTPException(HTTPException):
    """Custom HTTP Exception class for encapsulating API response details in exceptions."""

    def __init__(self, status_code: int, detail: Response):
        """
        Initializes a CustomHTTPException object.

        :param status_code: the status code of the exception
        :param detail: the response details of the exception
        """
        super().__init__(status_code=status_code, detail=detail.model_dump())


@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handles errors of type HTTPException, returning JSON responses with error details and status codes.

    :param request: the request object
    :param exc: the HTTPException object

    :return JSONResponse: the JSON response with error details and status code
    """
    return JSONResponse(content=exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Handles errors of type RequestValidationError,
    returning JSON responses with error details and status code 400.

    :param request: the request object
    :param exc: the RequestValidationError object

    :return JSONResponse: the JSON response with error details and status code 400
    """
    response = Response(
        error=str(exc.errors()),
        result=None
    )

    return JSONResponse(content=response.model_dump(), status_code=400)


@app.get("/")
def root():
    """Returns a welcome message."""
    return {"message": "Welcome to ChatGPT.MVP API."}


@app.get("/v1/status")
def status():
    """Returns the status of the API."""
    return {"status": "OK"}


@app.post("/v1/chat")
def chat(input_data: Input) -> dict:
    """
    Chat endpoint for interacting with the chatbot.

    :param input_data: input data for the chat endpoint
    :return: response data from the chat endpoint
    """

    try:

        # parse API input
        message = input_data.message
        personality = input_data.personality

        # create a ChatClient instance
        bot = ChatClient()

        # get response from chatbot
        response = bot.chat(message=message, personality=personality)

        # create response model on success
        result = Result(answer=response)
        response = Response(
            error=None,
            result=result
        )

        return response.model_dump()

    except Exception as error:

        # create response model on error
        response = Response(
            error=str(error),
            result=None
        )

        raise CustomHTTPException(status_code=500, detail=response)

    pass
