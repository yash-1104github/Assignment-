import random
from .schemas import Move

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

def validate_move(move: str, bomb_used: bool) -> Move:
    move = move.lower().strip()
    if move not in VALID_MOVES:
        return "invalid"
    if move == "bomb" and bomb_used:
        return "invalid"
    return move


def bot_move(bot_bomb_used: bool) -> Move:
    choices = ["rock", "paper", "scissors"]
    if not bot_bomb_used:
        choices.append("bomb")
    return random.choice(choices)


def resolve_round(user: Move, bot: Move) -> str:
    if user == "invalid":
        return "bot"
    if user == bot:
        return "draw"
    if user == "bomb":
        return "user"
    if bot == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    return "user" if rules[user] == bot else "bot"
