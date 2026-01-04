from pydantic import BaseModel
from typing import Literal

Move = Literal["rock", "paper", "scissors", "bomb", "invalid"]

class GameState(BaseModel):
    round: int = 1
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False
