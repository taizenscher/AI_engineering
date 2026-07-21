from llm.client import get_client
from logging_config import configure_logging
from agents.base import BaseAgent

if __name__=="__main__":
    print("running main app")
    configure_logging()
    # instantiate base model
    client = get_client()
    b_agent = BaseAgent("Base Agent", client=client)
    prompt = input(">>>")
    response = b_agent.run(prompt=prompt)
    print(response.content)
