import os

from openai import OpenAI, OpenAIError


class ChatGPTException(Exception):
    """Exception class for errors coming from ChatGPT."""

    def __init__(self, message: str, status_code: int):
        """
        Initializes a ChatGPTException object.

        :param message: the error message
        :param status_code: the status code of the error
        """
        super().__init__(message)
        self.status_code = status_code


class ChatGPT:
    """ChatGPT class to interact with the OpenAI ChatGPT model."""

    def __init__(self, model_name: str):
        """
        Initializes a ChatGPT object.

        :param model_name: OpenAI model name
        """

        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # initialize OpenAI client with API key
        self.model_name = model_name

    def chat(self, conversation: list[dict[str, str]]):
        """
        Chat with the ChatGPT model.

        :param conversation: a list of messages in the conversation
        :return: ChatGPT response on success
        """

        try:
            # make request to OpenAI API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=conversation,
                temperature=1,
                max_tokens=512,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response

        # handle OpenAI API errors
        except OpenAIError as error:
            error_message = str(error)
            status_code = error.status_code if hasattr(error, "status_code") else 500
            raise ChatGPTException(message=error_message, status_code=status_code)

        # handle other errors
        except Exception as error:
            error_message = f"Error while making request to OpenAI API: {error}"
            raise ChatGPTException(message=error_message, status_code=500)

        pass
