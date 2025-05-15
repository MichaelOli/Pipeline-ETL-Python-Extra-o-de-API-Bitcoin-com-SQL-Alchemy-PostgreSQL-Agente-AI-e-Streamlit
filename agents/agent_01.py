from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    description="Você é o melhor especialista de engenharia de dados do mundo!",
    tools=[DuckDuckGoTools()],     
    show_tool_calls=True,           
    markdown=True                   
)

# Prompt the agent
agent.tools.print_response("O que é o atacadão dia a dia?", stream=True)
