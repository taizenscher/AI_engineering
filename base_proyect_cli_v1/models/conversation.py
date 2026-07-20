from .message import Message

class Conversation:
    def __init__(self)->None:
        self._messages=[]

    def add_message(self, message:Message=None)->None:
        if not isinstance(message, Message):
            raise TypeError("Type error, message doesn't match class.")
        else:
            self._messages.append(message)

    def get_messages(self)->list[Message]:
        return self._messages

    def clear(self)->None:
        self._messages = []
