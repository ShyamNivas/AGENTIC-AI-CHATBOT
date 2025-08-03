from langchain.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    RETURNS THE LIST OF TOOLS TO BE USED IN THE CHATBOT

    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    CREATES AND RETURNS A TOOL NODE FOR THE GRAPH

    """
    return ToolNode(tools=tools)

