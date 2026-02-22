from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_classic import hub

load_dotenv()

# Use a valid Groq model
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

search_tool = DuckDuckGoSearchRun()

# The hwchase17/react prompt expects an "input" key
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=[search_tool], 
    verbose=True,
    handle_parsing_errors=True
)

if __name__ == "__main__":
    # ReAct agents traditionally use "input" as the key
    query = "What is the capital of France?"
    print(f"Executing query: {query}")
    try:
        response = agent_executor.invoke({"input": query})
        print(f"\nFinal Answer: {response['output']}")
    except Exception as e:
        print(f"Error during execution: {e}")