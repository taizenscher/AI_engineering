
class Message:
    def __init__(self, message:str=None, role:str=None)->None:
        self.id:int = None
        self.role:str = role
        self.content:str = message
        self.metadata:str = None

