import langchain
import subprocess
from langchain_groq import ChatGroq
import langgraph
from langgraph.graph import Graph
from uciscrape import scrape
from ucimlrepo import fetch_ucirepo
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

llm = ChatGroq(
    temperature=0,
    groq_api_key="",
    model="llama-3.1-70b-versatile"
)

def chatbot1(state):
    query=state["messages"][-2]
    print(query)
    prompt = """Extract only the id from the input. Just give the id number nothing else.
    For example:
    Output:235
    The input is 
    """ + query
    res = llm.invoke(prompt).content
    print(res)
    return {"messages":[res]}

def download(state):
    query=state["messages"][-1]
    print(query)
    dataset = fetch_ucirepo(id=int(query))
    X = dataset.data.features
    y = dataset.data.targets
    print(X)
    return {"messages": [f"Successfully downloaded dataset {query}"]}

def general_response(state):
    query=state["messages"][-2]
    print(query)
    prompt = "You are a helpful assistant. Provide a helpful response to their query.The query is" + query
    
    response = llm.invoke(prompt).content
    print(response)
    return {"messages": [response]}

def function_1(state: dict):
    message = state['messages']
    prompt = """Determine if this is a request to download a UCI dataset.
    If it is about downloading a dataset, respond with 'DATASET'.
    If it is a general question, respond with 'GENERAL'.
    Remember if the user requests some information about the datasets it is still a general question not a dataset question.

    
    Query: """ + message[-1]
    
    response = llm.invoke(prompt).content
    print(response)
    if "GENERAL" in response:
        return {"messages": ["GENERAL"]}
    return {"messages": ["DATASET"]}

def router(state):
    if "GENERAL" in state['messages'][-1]:
        return "general_response"
    return "agent1"

workflow = StateGraph(AgentState)

workflow.add_node("chatbot", function_1)
workflow.add_node("general_response", general_response)
workflow.add_node("agent1", chatbot1)
workflow.add_node("tool1", download)
workflow.add_edge(START, "chatbot")

workflow.add_conditional_edges(
    "chatbot",
    router
)

workflow.add_edge("agent1", "tool1")
workflow.add_edge("tool1", END)

workflow.add_edge("general_response", END)

app = workflow.compile()

