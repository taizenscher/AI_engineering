from .message import Message

class Conversation:
    def __init__(self)->None:
        self._messages=[]

    def add_message(self, message:Message=None)->None:
        self._messages.append(message)

    def get_messages(self)->list[Message]:
        if self._messages:
            return self._messages

    def clear(self)->None:
        self._messages = []
