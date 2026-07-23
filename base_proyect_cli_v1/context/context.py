from models.message import Message

class Context:
    def __init__(self, messages:list[Message]=None, system_prompt:str=None)->None:
        self.messages:list[Message] = messages
        self.system_prompt:str = system_prompt
        

        