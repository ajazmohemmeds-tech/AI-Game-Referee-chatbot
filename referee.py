from agent import RefereeAgent

def main():
    agent = RefereeAgent()
    print(agent.explain_rules())

    while not agent.state.game_over:
        user_input = input("Your move: ")
        print(agent.handle_turn(user_input))

if __name__ == "__main__":
    main()
