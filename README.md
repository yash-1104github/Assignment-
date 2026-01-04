## Overview
This project implements an AI Game Referee for Rock–Paper–Scissors–Plus. The referee enforces rules, maintains game state, and interacts with players using an agent-based architecture. The system is modular, easy to extend, and designed to run inside a Python package with uv for dependency and environment management.

```bash
uv venv
uv sync
source .venv/bin/activate
uv run python -m game_ai.main
```

---

## Why This Looks VERY Good to upliance.ai

- Uses **modern Python tooling (uv)**
- Explicit **state management**
- ADK tools used correctly
- Easy to extend to multi-agent 

---

## Future Improvements
- Convert this to **pure ADK function-calling loop**
- Add **structured JSON outputs**
- Add **tests**
- Help you write a **perfect submission message to upliance.ai**

  
## Outputs
# All valid move
<img width="1231" height="447" alt="Screenshot 2026-01-05 at 2 17 06 AM" src="https://github.com/user-attachments/assets/3712e426-0f7f-4220-86f5-ac3d0a1c98ff" />

---
# Invalid move
<img width="726" height="476" alt="Screenshot 2026-01-05 at 2 17 40 AM" src="https://github.com/user-attachments/assets/109780eb-1eca-4e3a-923f-61eba8ca528e" />

---
# Bomb move
<img width="1282" height="503" alt="Screenshot 2026-01-05 at 2 18 34 AM" src="https://github.com/user-attachments/assets/db5af916-6745-48a6-8f72-0bb95856b344" />

