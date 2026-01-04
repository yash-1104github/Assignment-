from google.adk.agents import Agent
from google.adk.runners import Runner
from google.genai import types
from google.adk.models import Gemini
from google.adk.sessions import InMemorySessionService
from .tools import validate_move, bot_move, resolve_round

agent = Agent(
    name="my_game",
    model="gemini-2.5-flash-lite",
    description="Referee for Rock Paper Scissors Plus",
    tools=[validate_move, bot_move, resolve_round],
)
