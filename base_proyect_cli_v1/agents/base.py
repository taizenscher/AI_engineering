from llm.client import LLMClient
from models.message import Message
from models.conversation import Conversation
from models.agentstate import AgentState
from logging_config import get_logger


class BaseAgent:
    def __init__(self, name, client) -> None:
        self.id: int = None
        self.name: str = name
        self.description: str = None
        # self.system_prompt: str = None
        self.logger = get_logger(__name__)
        
        self.state:AgentState = AgentState()
        self.conversation: Conversation = Conversation()
        self.llm_client: LLMClient = client

    def run(self, prompt:str) -> Message:
        self.logger.info("Agent response generation started")

        user_message:Message = Message(role="user", content=prompt)
        self.conversation.add_message(user_message)
        assistant_message:Message = self.__invoke_model(self.conversation)
        self.conversation.add_message(assistant_message)

        return assistant_message

    def __invoke_model(self, messages: Conversation) -> Message:
        self.logger.info("Agent invoking model")
        return self.llm_client.generate(
            messages=messages, system_prompt=self.state.system_prompt
        )

    def __process_response(self, resposne) -> None:
        self.logger.info("Processing response")
        print(resposne)
