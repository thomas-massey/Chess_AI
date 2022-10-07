# This is the engine for the program, we will be using OOP to create the game.

# We will also inclue the chess libary.

from random import randint
import random
from time import sleep
import chess
import Render
import os
# import AI

class Game:
    def __init__(self):
        # We create a new game.
        self.board = chess.Board()
        # We create a new render.
        self.render = Render.render(self.board)
        # Use the screen for getting who goes first
        player_colour = self.render.get_turn()
        # Load the graphics
        self.render.load_graphics()
        # We create a new AI.
        # self.generate_ai_move = AI.Chess_AI()
        # Game loop
        while self.board.is_game_over != False:
            # Find who's turn it is.
            if not player_colour == "AIBattle":
                if self.board.turn == True:
                    turn = "White"
                else:
                    turn = "Black"
            if ((player_colour == "Black") or (player_colour == "White")) and (player_colour == turn):
                legal_moves = self.board.generate_legal_moves()
                for move in legal_moves:
                    print(move)
                # Now listen for events.
                converted_move = self.render.get_events(self.board, turn)
            else:
                # Update the display as it will crash on input.
                self.render.update_display(self.board)
                # Basic form of random AI.
                ai_data = self.generate_ai_data()
                # Get a list of all the legal moves.
                moves = []
                legal_moves = self.board.generate_legal_moves()
                # # Pick a random move.
                for move in legal_moves:
                    moves.append(str(move))
                    print(move)
                # or use an ai
                #move = self.generate_ai_move(ai_data).get_move()



                if self.board.is_game_over() == True:
                    print("Game over!")
                    break
                converted_move = random.choice(moves)
            # Move will return a string of the form "a1b2"
            potencial_move = chess.Move.from_uci(converted_move)
            # If the move is legal, then we make the move.
            sleep(0.5)
            # Get the turn
            if self.board.turn == True:
                turn = "White"
            else:
                turn = "Black"
            if self.board.is_legal(potencial_move):
                print(turn + ": Move is legal")
                self.board.push(potencial_move)
                self.render.update_board(self.board, turn, converted_move)
            else:
                print(turn + ": Move is not legal")
        if self.board.is_checkmate():
            print("Checkmate! Player " + turn + " wins!")
        elif self.board.is_stalemate():
            print("Stalemate!")
        elif self.board.is_insufficient_material():
            print("Insufficient material!")
        elif self.board.is_seventyfive_moves():
            print("Seventyfive moves!")
        elif self.board.is_fivefold_repetition():
            print("Fivefold repetition!")
        elif self.board.is_variant_end():
            print("Variant end!")
        elif self.board.is_game_over():
            print("Game over!")
        else:
            print("Unknown error!")

    def generate_ai_data(self):
        # First feed it some data:
        # The format should always be a  array of 0's and 1's.
        # We will use the following format:
        # 0 = Empty
        # 1 = Occupied
        white_pawns = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("P"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_pawns.append(temp_row)
            temp_row = []
        black_pawns = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("p"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_pawns.append(temp_row)
            temp_row = []
        white_rooks = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("R"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_rooks.append(temp_row)
            temp_row = []
        black_rooks = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("r"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_rooks.append(temp_row)
            temp_row = []
        white_knights = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("N"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_knights.append(temp_row)
            temp_row = []
        black_knights = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("n"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_knights.append(temp_row)
            temp_row = []
        white_bishops = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("B"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_bishops.append(temp_row)
            temp_row = []
        black_bishops = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("b"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_bishops.append(temp_row)
            temp_row = []
        white_queens = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("Q"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_queens.append(temp_row)
            temp_row = []
        black_queens = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("q"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_queens.append(temp_row)
            temp_row = []
        white_kings = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("K"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            white_kings.append(temp_row)
            temp_row = []
        black_kings = []
        for j in range(1, 9):
            temp_row = []
            original_j = j
            for i in range(1, 9):
                # # Invert j so 8 is 1 and 1 is 8
                j = 9 - original_j
                # Convert the i to a letter.
                letter = chr(i + 96)
                if self.board.piece_at(chess.parse_square(str(letter) + str(j))) == chess.Piece.from_symbol("k"):
                    # Append 1
                    temp_row.append("1")
                else:
                    # Append 0
                    temp_row.append("0")
            black_kings.append(temp_row)
            temp_row = []
        if self.board.is_check:
            in_check = 1
        else:
            in_check = 0
        if self.board.has_kingside_castling_rights(chess.WHITE):
            white_kingside_castle = 1
        else:
            white_kingside_castle = 0
        if self.board.has_queenside_castling_rights(chess.WHITE):
            white_queenside_castle = 1
        else:
            white_queenside_castle = 0
        if self.board.has_kingside_castling_rights(chess.BLACK):
            black_kingside_castle = 1
        else:
            black_kingside_castle = 0
        if self.board.has_queenside_castling_rights(chess.BLACK):
            black_queenside_castle = 1
        else:
            black_queenside_castle = 0
        if self.board.has_legal_en_passant():
            en_passant_possible = 1
        else:
            en_passant_possible = 0
        # Define endgame states
        is_draw = ""
        # Now print all the data.
        print("White pawns: \n" + str(white_pawns) + "\nBlack pawn: \n" + str(black_pawns) + "\nWhite rooks: \n" + str(white_rooks) + "\nBlack rooks: \n" + str(black_rooks) + "\nWhite knights: \n" + str(white_knights) + "\nBlack knights: \n" + str(black_knights) + "\nWhite bishops: \n" + str(white_bishops) + "\nBlack bishops: \n" + str(black_bishops) + "\nWhite queens: \n" + str(white_queens) + "\nBlack queens: \n" + str(black_queens) + "\nWhite kings: \n" + str(white_kings) + "\nBlack kings: \n" + str(black_kings))
        
    def get_legal_moves(self):
        return self.board.legal_moves