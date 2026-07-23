from models.agent_state import AgentState
from models.conversation import Conversation
from context import Context
class ContextBuilder:
    def build(state:AgentState=None, conversation:Conversation=None)->Context:
        return Context(state=state, conversation=conversation)