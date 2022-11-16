import chess

class AI:
    def __init__(self):
        pass

    def generate_BF3_best_move(self, board, possible_moves, turn):
        # print("AI is thinking...")
        best_points = 0
        best_move = None
        possible_board = None
        original_score = self.calculate_score(board, turn)
        for possible_move1 in possible_moves:
            board1 = self.make_move(board, possible_move1)
            possible_moves = self.get_possible_moves(board1)
            for possible_move2 in possible_moves:
                board2 = self.make_move(board1, possible_move2)
                possible_moves = self.get_possible_moves(board2)
                for possible_move3 in possible_moves:
                    possible_board = self.make_move(board2, possible_move3)
                    potential_points = self.calculate_score(possible_board, turn)
                    if potential_points > best_points:
                        best_points = potential_points
                        best_move = possible_move1

        return best_move
    
    def generate_BF5_best_move(self, board, possible_moves, turn):
        # print("AI is thinking...")
        best_points = 0
        best_move = None
        possible_board = None
        original_score = self.calculate_score(board, turn)
        for possible_move1 in possible_moves:
            board1 = self.make_move(board, possible_move1)
            possible_moves = self.get_possible_moves(board1)
            for possible_move2 in possible_moves:
                board2 = self.make_move(board1, possible_move2)
                possible_moves = self.get_possible_moves(board2)
                for possible_move3 in possible_moves:
                    board3 = self.make_move(board2, possible_move3)
                    possible_moves = self.get_possible_moves(board3)
                    for possible_move4 in possible_moves:
                        board4 = self.make_move(board3, possible_move4)
                        possible_moves = self.get_possible_moves(board4)
                        for possible_move5 in possible_moves:
                            possible_board = self.make_move(board4, possible_move5)
                            potential_points = self.calculate_score(possible_board, turn)
                            if potential_points > best_points:
                                best_points = potential_points
                                best_move = possible_move1

        return best_move

    def generate_AIA_best_move(self, board, possible_moves, turn):
        pass

    def generate_MM3_best_move(self, board, possible_moves, turn):
        # This is where we make use of the maxmin algorithum
        # It works like brute force, but we find the best point move, then the best defensive move.
        best_points = 0
        best_move = None
        possible_board = None
        original_score = self.calculate_score(board, turn)
        for possible_move in possible_moves:
            possible_board = self.make_move(board, possible_move)
            potential_points = self.calculate_score(possible_board, turn)
            for possible_move2 in self.get_possible_moves(possible_board):
                possible_board2 = self.make_move(possible_board, possible_move2)
                # Now we try to minimise the opponents score
                potential_points -= ((self.calculate_score) * -1)
                for possible_move3 in self.get_possible_moves(possible_board2):
                    possible_board3 = self.make_move(possible_board2, possible_move3)
                    # Now we try to minimise the opponents score
                    potential_points -= ((self.calculate_score) * -1)
                    if potential_points > best_points:
                        best_points = potential_points
                        best_move = possible_move
        return best_move

    def make_move(self, board, move):
        # Convert the board to a fen string.
        fen = board.fen()
        board = chess.Board(fen)
        move = chess.Move.from_uci(str(move))
        board.push(move)
        return board

    def get_possible_moves(self, board):
        return board.legal_moves

    def calculate_score(self, board, turn):
        # This is a very basic score calculator.
        # It just counts the number of pieces.
        # The more pieces you have, the better.
        # The score is negative if it is black's turn.
        score = 0
        for piece in board.piece_map().values():
            if piece.color == chess.WHITE:
                if piece.piece_type == chess.PAWN:
                    score += 1
                elif piece.piece_type == chess.KNIGHT:
                    score += 3
                elif piece.piece_type == chess.BISHOP:
                    score += 3
                elif piece.piece_type == chess.ROOK:
                    score += 5
                elif piece.piece_type == chess.QUEEN:
                    score += 9
                elif piece.piece_type == chess.KING:
                    score += 100
            else:
                if piece.piece_type == chess.PAWN:
                    score -= 1
                elif piece.piece_type == chess.KNIGHT:
                    score -= 3
                elif piece.piece_type == chess.BISHOP:
                    score -= 3
                elif piece.piece_type == chess.ROOK:
                    score -= 5
                elif piece.piece_type == chess.QUEEN:
                    score -= 9
                elif piece.piece_type == chess.KING:
                    score -= 100
        if turn == "Black":
            score *= -1
        return score