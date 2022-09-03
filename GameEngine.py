# This is the engine for the program, we will be using OOP to create the game.

# We will also inclue the chess libary.

from random import randint
import random
from time import sleep
import chess
import Render
import os

class Game:
    def __init__(self):
        # We create a new game.
        self.board = chess.Board()
        # We create a new render.
        self.render = Render.render(self.board)
        while True:
            player_colour = input("What colour would you like to play as, White, Black or Random? (w/b/r): ")
            if player_colour == "w":
                player_colour = "White"
                break
            elif player_colour == "b":
                player_colour = "Black"
                break
            elif player_colour == "r":
                type = randint(0, 1)
                if type == 0:
                    player_colour = "White"
                else:
                    player_colour = "Black"
        # Game loop
        while self.board.is_checkmate != False:
            # Find who's turn it is.
            if self.board.turn == True:
                turn = "White"
            else:
                turn = "Black"
            if turn == player_colour:
                legal_moves = self.board.generate_legal_moves()
                for move in legal_moves:
                    print(move)
                # Now listen for events.
                converted_move = self.render.get_events(self.board, turn)
            else:
                # Basic form of random AI.
                # Get a list of all the legal moves.
                moves = []
                legal_moves = self.board.generate_legal_moves()
                # Pick a random move.
                for move in legal_moves:
                    moves.append(str(move))
                    print(move)
                if len(moves) == 0:
                    print("Checkmate!")
                    break
                converted_move = random.choice(moves)
            # Move will return a string of the form "a1b2"
            potencial_move = chess.Move.from_uci(converted_move)
            # If the move is legal, then we make the move.
            sleep(0.5)
            if self.board.is_legal(potencial_move):
                print(turn + ": Move is legal")
                self.board.push(potencial_move)
                self.render.update_board(self.board, turn)
            else:
                print(turn + ": Move is not legal")


    def get_legal_moves(self):
        return self.board.legal_moves