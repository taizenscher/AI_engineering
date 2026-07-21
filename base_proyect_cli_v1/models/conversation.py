from .message import Message


class Conversation:
    def __init__(self) -> None:
        self._messages:list[Message] = []

    def add_message(self, message: Message = None) -> None:
        if not isinstance(message, Message):
            raise TypeError("Type error, message doesn't match class.")
        self._messages.append(message)

    def get_messages(self) -> list[Message]:
        messages = []
        for i,message in enumerate(self._messages):
            messages.append({"role":message.role, "content":message.content})
        return messages

    def clear(self) -> None:
        self._messages = []
