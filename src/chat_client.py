import uuid

from src.llm import ChatGPT
from src.prompt_resolver import PromptResolver
from src.utils import create_logger


class ChatClient:
    """ChatClient class to interact with the ChatGPT model."""

    def __init__(self):
        """Initializes a ChatClient object."""

        self.logger = create_logger()
        self.session_id = str(uuid.uuid4())  # create a unique ID for the chat session

        self.model = ChatGPT(model_name="gpt-3.5-turbo")
        self.prompt_resolver = PromptResolver()

    def chat(self, message: str, personality: str) -> str:
        """
        Chat with the ChatGPT model.

        :param message: user message
        :param personality: personality for ChatGPT
        :return:
        """

        self.logger.info(f"STARTED CHAT SESSION {self.session_id}")

        system_prompt = self.get_system_prompt(personality=personality)

        # format input messages to ChatGPT
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
        self.logger.info(f"INPUT: {messages}")

        # get and parse response from ChatGPT
        response = self.model.chat(conversation=messages).choices[0].message.content
        self.logger.info(f"OUTPUT: {response}")

        self.logger.info(f"ENDED CHAT SESSION {self.session_id}")

        return response

    def get_system_prompt(self, personality: str) -> str:
        """
        Construct the system prompt for ChatGPT.

        :param personality: personality for ChatGPT
        :return: a completed system prompt
        """

        system_message_filepath = "src/prompts/system.liquid"
        system_message = self.prompt_resolver.make_prompt(filename=system_message_filepath,
                                                          personality=personality).body

        return system_message
