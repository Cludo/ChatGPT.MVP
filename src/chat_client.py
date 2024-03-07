from src.llm import ChatGPT
from src.prompt_resolver import PromptResolver


class ChatClient:

    def __init__(self):
        self.model = ChatGPT(model_name="gpt-3.5-turbo")
        self.prompt_resolver = PromptResolver()

    def chat(self, message: str, personality: str) -> str:

        system_prompt = self.get_system_prompt(personality=personality)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]

        response = self.model.chat(conversation=messages)

        return response.choices[0].message.content

    def get_system_prompt(self, personality: str) -> str:

        system_message_filepath = "src/prompts/system.liquid"
        system_message = self.prompt_resolver.make_prompt(filename=system_message_filepath,
                                                          personality=personality).body

        return system_message

