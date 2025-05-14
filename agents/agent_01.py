from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize the agent with an LLM via Groq and DuckDuckGoTools
agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    description="Você é o melhor especialista de engenharia de dados do mundo!",
    tools=[DuckDuckGoTools()],      # Add DuckDuckGo tool to search the web
    show_tool_calls=True,           # Shows tool calls in the response, set to False to hide
    markdown=True                   # Format responses in markdown
)

# Prompt the agent to fetch a breaking news story from New York
agent.tools.print_response("O que é o atacadão dia a dia?", stream=True)