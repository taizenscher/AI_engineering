from llm.client import LLMClient
from models.response import AgentResponse

class BaseAgent:
    def __init__(self, name, client)->None:
        self.id:int = None
        self.name:str = name
        self.description:str = None
        self.llm_client:LLMClient = client
        self.system_prompt:str = None

    def run(self, prompt)->AgentResponse:
        response:AgentResponse = self.llm_client.generate(prompt, self.system_prompt)
        return response

