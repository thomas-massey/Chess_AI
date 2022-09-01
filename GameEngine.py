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
            # Now listen for events.
            move = self.render.get_events(self.board, turn)
            # Convert from (row, col) to (letter, number) where (7,0) is a1 and (0,7) is h8
            letter_pre = chr(abs(int(move[1][1]))+97)
            letter_post = chr(abs(int(move[0][1]))+97)
            number_pre = abs(int(move[0][0])-8)
            number_post = abs(int(move[1][0])-8)
            converted_move = letter_pre+str(number_pre)+letter_post+str(number_post)
            potencial_move = chess.Move.from_uci(converted_move)
            # If the move is legal, then we make the move.
            possible_moves = self.board.legal_moves
            if self.board.is_legal(potencial_move):
                print(turn + ": Move is legal")
                self.board.push(potencial_move)
                self.render.update_board(self.board, turn)
            else:
                print(turn + ": Move is not legal")


    def get_legal_moves(self):
        return self.board.legal_moves