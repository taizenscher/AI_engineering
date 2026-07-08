from llm.client import get_client

if __name__=="__main__":
    print("running main app")
    # instantiate base model
    client = get_client()
    prompt = input(">>>")
    response = client.generate(prompt)
    print(response)
