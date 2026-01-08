from state import GameState
from tools import validate_move, resolve_round, update_game_state

class RefereeAgent:
    def __init__(self):
        self.state = GameState()

    def explain_rules(self):
        return (
            "Best of 3 rounds.\n"
            "Moves: rock, paper, scissors, bomb.\n"
            "Bomb beats all but can be used once.\n"
            "Bomb vs bomb is a draw.\n"
            "Invalid input wastes the round."
        )

    def choose_bot_move(self):
        if not self.state.bot_bomb_used and self.state.round == 3:
            return "bomb"
        return "rock"

    def handle_turn(self, user_input: str):
        state = self.state

        valid, result = validate_move(user_input, True, state)
        if not valid:
            update_game_state(state, None, None, None)
            return f"Round {state.round - 1}: Invalid input. Round wasted."

        user_move = result
        bot_move = self.choose_bot_move()

        winner = resolve_round(user_move, bot_move)
        update_game_state(state, user_move, bot_move, winner)

        response = (
            f"Round {state.round - 1}\n"
            f"You: {user_move} | Bot: {bot_move}\n"
            f"Winner: {winner.upper()}\n"
            f"Score — You: {state.user_score}, Bot: {state.bot_score}"
        )

        if state.game_over:
            if state.user_score > state.bot_score:
                response += "\nFinal Result: USER WINS"
            elif state.bot_score > state.user_score:
                response += "\nFinal Result: BOT WINS"
            else:
                response += "\nFinal Result: DRAW"

        return response
