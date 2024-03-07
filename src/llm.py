import os

from openai import OpenAI, OpenAIError


class ChatGPTException(Exception):

    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code


class ChatGPT:

    def __init__(self, model_name: str):

        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_name = model_name

    def chat(self, conversation: list[dict[str, str]]):

        try:
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

        except OpenAIError as error:
            error_message = str(error)
            status_code = error.status_code if hasattr(error, "status_code") else 500
            raise ChatGPTException(message=error_message, status_code=status_code)

        except Exception as error:
            error_message = f"Error while making request to OpenAI API: {error}"
            raise ChatGPTException(message=error_message, status_code=500)

        pass
