class AgentState:
    def __init__(self)->None:
        self.system_prompt: str | None = None
        self.iteration: int = 0