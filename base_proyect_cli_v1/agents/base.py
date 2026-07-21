from llm.client import LLMClient
from models.message import Message
from models.conversation import Conversation
from logging_config import get_logger


class BaseAgent:
    def __init__(self, name, client) -> None:
        self.id: int = None
        self.name: str = name
        self.description: str = None
        self.llm_client: LLMClient = client
        self.system_prompt: str = None
        self.logger = get_logger(__name__)
        self.conversation: Conversation = Conversation()

    def run(self, prompt:str) -> Message:
        self.logger.info("Agent response generation started")

        user_message:Message = Message(role="user", content=prompt)
        self.conversation.add_message(user_message)
        assistant_message:str = self.__invoke_model(self.conversation)
        # assistant_message:Message = Message(role="assistant", content=response)
        self.conversation.add_message(assistant_message)

        return assistant_message.content

    def __invoke_model(self, conversation: list[Message]) -> str:
        self.logger.info("Agent invoking model")
        return self.llm_client.generate(
            messages=conversation, system_prompt=self.system_prompt
        )

    def __process_response(self, resposne) -> None:
        self.logger.info("Processing response")
        print(resposne)
