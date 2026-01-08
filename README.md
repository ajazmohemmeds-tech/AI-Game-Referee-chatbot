This project implements a minimal AI referee chatbot that runs a short game of Rock–Paper–Scissors–Plus between a user and a bot in a command-line interface.
The bot enforces game rules, tracks state across turns, and provides clear round-by-round feedback.

The implementation focuses on correct logic, explicit state modeling, and clean separation of concerns, rather than UI or polish.

⸻

Game Rules
	•	The game is best of 3 rounds
	•	Valid moves:
	•	rock
	•	paper
	•	scissors
	•	bomb (can be used once per player)
	•	bomb beats all other moves
	•	bomb vs bomb results in a draw
	•	Invalid input wastes the round
	•	The game automatically ends after 3 rounds

⸻

Architecture & Design

State Model
	•	Game state is stored in a dedicated GameState object
	•	Tracks:
	•	Current round
	•	User score and bot score
	•	Bomb usage per player
	•	Game termination status
	•	State is not stored in prompts and persists across turns

Agent Design
	•	A single Referee Agent manages:
	•	Rule explanation
	•	User input handling
	•	Tool coordination
	•	Response generation
	•	The agent does not directly mutate state

Tools Used

Explicit tools are defined to enforce separation of concerns:
	•	validate_move
Validates user input and enforces constraints (e.g., bomb usage)
	•	resolve_round
Determines the outcome of a round based on the game rules
	•	update_game_state
Mutates game state (scores, rounds, bomb usage, game end)

All rule enforcement and state mutation occur through tools.

⸻

Execution Environment
	•	Language: Python 3
	•	Interface: Command Line (CLI)
	•	No usage of:
	•	Databases
	•	External APIs
	•	UI frameworks
	•	Long-running servers
  Tradeoffs & Limitations
	•	Bot strategy is deterministic for clarity and auditability
	•	Input parsing is string-based (no NLP intent inference)
	•	Focus is on correctness and structure, not UX polish

⸻

Possible Improvements
	•	Smarter or adaptive bot strategy
	•	Structured schemas for tool inputs/outputs
	•	Unit tests for tools and state transitions
	•	Replay or audit logging of game rounds

⸻

Summary

This project demonstrates:
	•	Correct rule enforcement
	•	Explicit and persistent state modeling
	•	Clean agent/tool separation
	•	Clear, maintainable Python design

It is intentionally minimal and easy to reason about.
