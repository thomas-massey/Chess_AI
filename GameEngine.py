# This is the engine for the program, we will be using OOP to create the game.

# We will also inclue the chess libary.

import chess
import Render

class Game:
    def __init__(self):
        # We create a new game.
        self.board = chess.Board()
        # We create a new render.
        self.render = Render.render(self.board)
        

    def get_legal_moves(self):
        return self.board.legal_moves