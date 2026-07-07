from ollama import chat
from ollama import ChatResponse
from config.settings import settings

class LLMClient:
    def __init__(self):
        self.model = settings.model

    def generate(
            self,
            prompt: str,
            system_prompt: str | None = None,
        ) -> str:
        response: ChatResponse = chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response.message.content

def get_client() -> LLMClient:
    client = LLMClient()
    return client


