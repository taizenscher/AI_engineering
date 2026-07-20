from llm.client import LLMClient
from base_proyect_cli_v1.models.message import Message
from base_proyect_cli_v1.models.conversation import Conversation
from logging_config import get_logger

class BaseAgent:
    def __init__(self, name, client)->None:
        self.id:int = None
        self.name:str = name
        self.description:str = None
        self.llm_client:LLMClient = client
        self.system_prompt:str = None
        self.logger = get_logger(__name__)
        self.conversation:Conversation = Conversation()

    def run(self, prompt)->Message:
        self.logger.info("Agent response generation started")

        user_message = Message(role="user", message=prompt)
        self.conversation.add_message(user_message)
        response:Message = self.__invoke_model(
            prompt=user_message.content,
            role=user_message.role
            )
        assistant_message = Message(
            role="assistant",
            content=response
        )
        self.conversation.add_message(assistant_message)

        return self.assistant_message

    def __prepare_prompt(self):
        pass

    def __invoke_model(self, prompt, role)->Message:
        self.logger.info("Agent invoking model")
        return self.llm_client.generate(
            prompt=prompt, role=role, system_prompt=self.system_prompt
            )

    def __process_response(self, resposne)->None: 
        self.logger.info("Processing response")
        print(resposne)