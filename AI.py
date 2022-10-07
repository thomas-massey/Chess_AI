# This is the AI module for a game of chess.
# It will generate a move and at the end of the game it will
# generate a report on the game.
# This means that it will be a generation AI.
# It will be aware of all past moves

# Imports - we will use openAI gym for this

import gym

class Chess_AI:
    # We will use multiple instances of moves and when a game is over - we will output a report.
    # Then we can use the report for the next generation to learn from.
    def __init__(self):
        # Make my own environment
        self.env = gym.make('Chess-v0')
        self.env.reset()

        # Save file for the AI
        self.save_file = "AI.save"

    # We will pass through all of the possible moves (strings) and all of the game state details (one-hot encoded)

    def generate_move(self, game_state, history):
        # History will 

        # We will use the openAI gym library to generate a move
        # We will pass through all of the possible moves (strings) and all of the game state details (one-hot encoded)
        # We will then use the openAI gym library to generate a move
        # We will then return the move
        self.game_state = game_state
        self.history = history
        self.env.step()
        self.env.render()
        self.env.close()
