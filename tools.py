from state import GameState

def validate_move(move: str, is_user: bool, state: GameState):
    move = move.lower().strip()
    valid_moves = {"rock", "paper", "scissors", "bomb"}

    if move not in valid_moves:
        return False, "Invalid move"

    if move == "bomb":
        if is_user and state.user_bomb_used:
            return False, "User bomb already used"
        if not is_user and state.bot_bomb_used:
            return False, "Bot bomb already used"

    return True, move


def resolve_round(user_move: str, bot_move: str):
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }

    return "user" if (user_move, bot_move) in wins else "bot"


def update_game_state(state: GameState, user_move, bot_move, result):
    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    if result == "user":
        state.user_score += 1
    elif result == "bot":
        state.bot_score += 1

    state.round += 1
    if state.round > state.max_rounds:
        state.game_over = True
