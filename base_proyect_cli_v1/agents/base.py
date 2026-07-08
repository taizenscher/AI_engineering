from ollama import Client
from models.response import AgentRespose

class BaseAgent:
    def __init__(self, name)->None:
        self.id:int = None
        self.name:str = name
        self.description:str = None
        self.llm_client:Client = None
        self.system_prompt:str = None

    def run(self, prompt)->AgentResponse:
        resposne:AgentResponse = self.llm_client.generate(prompt, self.system_prompt)
        return response

