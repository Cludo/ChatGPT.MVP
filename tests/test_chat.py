import sys
import os

working_directory = os.getcwd()
sys.path.append(working_directory)
from src.chat_client import ChatClient


def test_chat():
    """ Test the chat method of the ChatClient class. """

    # create a ChatClient instance
    bot = ChatClient()

    # define input to chatbot
    message = "Hi, how are you today?"
    personality = "Gandalf"

    # get response from chatbot
    response = bot.chat(message=message, personality=personality)

    # assert response is a string
    assert isinstance(response, str)

    pass
