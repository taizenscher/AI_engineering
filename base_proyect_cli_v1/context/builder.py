from models.agent_state import AgentState
from models.conversation import Conversation

class ContextBuilder:
    def __init__(self, state:AgentState=None, conversation:Conversation=None)->None:
        self.conversation: Conversation = conversation
        self.state: AgentState = state

    def build(self):
        pass