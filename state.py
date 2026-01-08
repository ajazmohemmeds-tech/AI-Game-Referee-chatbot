from dataclasses import dataclass
@dataclass
class GameState:
    round: int = 1
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False
    max_rounds: int = 3
    game_over: bool = False
