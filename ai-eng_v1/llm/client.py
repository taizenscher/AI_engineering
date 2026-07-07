from ollama import ChatResponse, Client
from config.settings import settings

class LLMClient:
    def __init__(self) -> None:
        self.client = Client(host=settings.ollama_host)

    def generate(
            self,
            prompt: str,
            system_prompt: str | None = None,
        ) -> str:
        response: ChatResponse = self.client.chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response.message.content

def get_client() -> LLMClient:
    client = LLMClient()
    return client


