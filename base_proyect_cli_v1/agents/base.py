from llm.client import LLMClient
from models.response import AgentResponse
from logging_config import get_logger

class BaseAgent:
    def __init__(self, name, client)->None:
        self.id:int = None
        self.name:str = name
        self.description:str = None
        self.llm_client:LLMClient = client
        self.system_prompt:str = None
        self.logger = get_logger(__name__)

    def run(self, prompt)->AgentResponse:
        self.logger.info("Agent response generation started")
        
        response:AgentResponse = self.__invoke_model(prompt)
        response = self._invoke_model(prompt)
        response = self._process_response(response)

        return response

    def __prepare_prompt(self):
        pass

    def __invoke_model(self, prompt)->AgentResponse:
        self.logger.info("Agent invoking model")
        return self.llm_client.generate(prompt, self.system_prompt)

    def __process_response(self, resposne)->None: 
        self.logger.info("Processing response")
        print(resposne)