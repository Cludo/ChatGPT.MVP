import uuid

from src.llm import ChatGPT
from src.prompt_resolver import PromptResolver
from src.utils import create_logger


class ChatClient:

    def __init__(self):

        self.logger = create_logger()
        self.session_id = str(uuid.uuid4())

        self.model = ChatGPT(model_name="gpt-3.5-turbo")
        self.prompt_resolver = PromptResolver()

    def chat(self, message: str, personality: str) -> str:

        self.logger.info(f"STARTED CHAT SESSION {self.session_id}")

        system_prompt = self.get_system_prompt(personality=personality)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
        self.logger.info(f"INPUT: {messages}")

        response = self.model.chat(conversation=messages).choices[0].message.content
        self.logger.info(f"OUTPUT: {response}")

        self.logger.info(f"ENDED CHAT SESSION {self.session_id}")

        return response

    def get_system_prompt(self, personality: str) -> str:

        system_message_filepath = "src/prompts/system.liquid"
        system_message = self.prompt_resolver.make_prompt(filename=system_message_filepath,
                                                          personality=personality).body

        return system_message
