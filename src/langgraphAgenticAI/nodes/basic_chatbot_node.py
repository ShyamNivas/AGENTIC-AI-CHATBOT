from src.langgraphAgenticAI.state.state import State

class BasicChatbotNode:
    """
    BASIC CHATBOT LOGIC IMPLEMENTATION

    """
    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:
        """
        PROCESS THE INPUT STATE AND GENERATE A CHATBOT RESPONSE
        
        """
        return{"messages":self.llm.invoke(state["messages"])}