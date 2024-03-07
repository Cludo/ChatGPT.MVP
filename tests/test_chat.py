import sys
import os

working_directory = os.getcwd()
sys.path.append(working_directory)
from src.chat_client import ChatClient


def test_chat():

    bot = ChatClient()

    message = "Hi, how are you today?"
    personality = "Gandalf"
    response = bot.chat(message=message, personality=personality)

    assert isinstance(response, str)

    pass
