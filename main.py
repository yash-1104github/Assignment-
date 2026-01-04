import os
from .agent import agent
from .game_state import game_state
from .tools import validate_move, bot_move, resolve_round

print(
    """
Welcome to Rock–Paper–Scissors–Plus!
Rules:
1. Best of 3 rounds
2. rock, paper, scissors, bomb
3. Bomb beats all but can be used once
4. Invalid move wastes the round
"""
)


while game_state.round <= 3:
    print(f"\nRound {game_state.round}")
    user_input = input("Your move: ")

    user_move = validate_move(user_input, game_state.user_bomb_used)
    if user_move == "bomb":
        game_state.user_bomb_used = True

    bot_choice = bot_move(game_state.bot_bomb_used)
    if bot_choice == "bomb":
        game_state.bot_bomb_used = True

    winner = resolve_round(user_move, bot_choice)

    if winner == "user":
        game_state.user_score += 1
    elif winner == "bot":
        game_state.bot_score += 1

    print(f"You played: {user_move}")
    print(f"Bot played: {bot_choice}")
    print(f"Round winner: {winner}")

    game_state.round += 1

print("\nFinal Result:")
print(f"You: {game_state.user_score} | Bot: {game_state.bot_score}")

if game_state.user_score > game_state.bot_score:
    print("You win, congrates")
elif game_state.user_score < game_state.bot_score:
    print("Bot wins, Better luck next time, my friend")
else:
    print("It is a draw")
