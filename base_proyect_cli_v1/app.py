from llm.client import get_client
from logging_config import configure_logging

if __name__=="__main__":
    print("running main app")
    configure_logging()
    # instantiate base model
    client = get_client()
    prompt = input(">>>")
    response = client.generate(prompt)
    print(response)
