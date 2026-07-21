class Message:
    def __init__(self, content: str = None, role: str = None) -> None:
        self.id: int = None
        self.role: str = role
        self.content: str = content
        self.metadata: dict | None = None
