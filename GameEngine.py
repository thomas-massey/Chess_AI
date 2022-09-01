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
        # Game loop
        while self.board.is_checkmate != False:
            # Now listen for events.
            move = self.render.get_events()
            # Convert from (row, col) to (letter, number) where (7,0) is a1 and (0,7) is h8
            letter_pre = chr(abs(int(move[0][0])-7)+96)
            letter_post = chr(abs(int(move[1][0])-7)+96)
            number_pre = abs(int(move[0][1])-7)
            number_post = abs(int(move[1][1])-7)
            converted_move = letter_pre+str(number_pre)+letter_post+str(number_post)
            potencial_move = chess.Move.from_uci(converted_move)
            # If the move is legal, then we make the move.
            possible_moves = self.board.legal_moves
            for moves in possible_moves:
                if moves == potencial_move:
                    print("Move is legal")
                else:
                    print("Move is not legal")
                    


    def get_legal_moves(self):
        return self.board.legal_moves