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
            # Find who's turn it is.
            if self.board.turn == chess.WHITE:
                turn = "White"
            else:
                turn = "Black"
            # Render who's turn it is.
            self.render.show_turn(turn)
            # Now listen for events.
            move = self.render.get_events(self.board, turn)
            # Convert from (row, col) to (letter, number) where (7,0) is a1 and (0,7) is h8
            # Move will return a string of the form "a1b2"
            letter_pre = move[0:1]
            letter_post = move[2:3]
            number_pre = move[1:2]
            number_post = move[3:4]
            converted_move = letter_pre+str(number_pre)+letter_post+str(number_post)
            potencial_move = chess.Move.from_uci(converted_move)
            # If the move is legal, then we make the move.
            if self.board.is_legal(potencial_move):
                print(turn + ": Move is legal")
                self.board.push(potencial_move)
                self.render.update_board(self.board, turn)
            else:
                print(turn + ": Move is not legal")


    def get_legal_moves(self):
        return self.board.legal_moves