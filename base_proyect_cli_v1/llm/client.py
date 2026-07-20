from ollama import ChatResponse, Client
from config.settings import settings
from logging_config import get_logger

class LLMClient:
    def __init__(self) -> None:
        self.ollama_host:str = settings.ollama_host
        self.ollama_model:str = settings.ollama_model
        self.temperature:float = settings.temperature
        self.timeout:int = settings.timeout
        self.embedding_model:str = settings.embedding_model
        self.vector_db:str = settings.vector_db
        self.logger = get_logger(__name__)
        self._establish_connection()

    def _establish_connection(self)->None:
        try:
            self.client:Client = Client(host=settings.ollama_host)
        except Exception as e:
            self.logger.critical("Connection couldn't be established")
            self.logger.exception(e)
            raise

    def generate(
            self,
            prompt: str,
            role: str = None, 
            system_prompt: str | None = None,
        ) -> str:
        self.logger.info("Model generating response")
        response: ChatResponse = self.client.chat(model=self.ollama_model, messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": role,
                "content": prompt
            }
        ])
        return response.message.content

def get_client() -> LLMClient:
    client = LLMClient()
    return client


