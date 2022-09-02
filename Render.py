# This is the where the rendering of the game is done. We will be using OOP

# Imports

from time import sleep
import pygame

class render:
    def __init__(self, game):
        # Load the game
        self.game = game
        # Load graphics
        self.load_graphics()
        return
    
    def load_images(self):
        pieces = ["Nb", "Rb", "Bb", "Qb", "Kb", "Pb", "Pw", "Rw", "Nw", "Kw", "Qw", "Bw"]
        for piece in pieces:
            # Load the image and then convert it to be a transparent png
            image_loading = pygame.image.load("C:\\Users\\thoma\\OneDrive - Ardingly College\\Lessons\\U6\\Computer Science\\Personal Projects\\Chess_AI\\images\\" + piece + ".png").convert_alpha()
            self.IMAGES[piece] = pygame.transform.scale(image_loading, (self.WIDTH / 8, self.HEIGHT / 8))
        # We can now access an image by saying 'IMAGES['Pw']'

    def draw_board(self):
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.init()
        pygame.display.set_caption("Chess")
        # Draw the board
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.surface, self.RED, (row * self.WIDTH / 8, col * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
                else:
                    pygame.draw.rect(self.surface, self.GREEN, (row * self.WIDTH / 8, col * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
        pygame.display.update()

    def draw_pieces(self):
        # Draw the pieces
        board = str(self.game)
        board = board.replace(" ", "")
        board = board.replace("\n", "")
        for row in range(8):
            for col in range(8):
                piece = board[(row * 8) + col]
                if piece == ".":
                    pass
                elif piece.isupper():
                    self.surface.blit(self.IMAGES[piece+"w"], (col * self.WIDTH / 8, row * self.HEIGHT / 8))
                else:
                    self.surface.blit(self.IMAGES[piece.upper()+"b"], (col * self.WIDTH / 8, row * self.HEIGHT / 8))
        # Update who's turn in the GUI
        self.show_turn(self.game.turn)
        pygame.display.update()
    
    def get_events(self, game, turn):
        clicked_square = ()
        player_squares = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row = int(pygame.mouse.get_pos()[1] / (self.HEIGHT / 8))
                    col = int(pygame.mouse.get_pos()[0] / (self.WIDTH / 8))
                    # Check if the square is owned by the player and moveable
                    if len(player_squares) == 1:
                        if (chr(int(col)+97) + str(abs((int(row)-8)))) == player_squares[0]:
                            self.reload_graphics()
                            player_squares = []
                        else:
                            destination = chr(int(col)+97) + str(abs((int(row)-8)))
                            full_move = (origin+destination)
                            for move in game.legal_moves:
                                if full_move in str(move):
                                    player_squares.append(destination)
                                    print(full_move)
                                    return full_move
                    elif len(player_squares) == 0:
                        legal_moves = game.legal_moves
                        origin = chr(int(col)+97) + str(abs((int(row)-8)))
                        print(origin)
                        more_moves = [] # Where the possible moves are stored
                        place_found = False # If the origin square is found
                        for move in legal_moves:
                            original_move = str(move)
                            # Get the first two chracters of the move
                            move=str(move)[:2]
                            if origin in move:
                                if not place_found:
                                    player_squares.append(origin)
                                    place_found = True
                                more_moves.append(original_move)
                        print(player_squares)
                        # Now render the possible locations
                        for move in more_moves:
                            row = abs(int(str(move)[3:4])-8)
                            col = ord(str(move)[2:3]) - 97
                            pygame.draw.rect(self.surface, self.BLUE, (col * self.WIDTH / 8, row * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
                
                pygame.time.Clock().tick(self.MAX_FPS)
                pygame.display.flip()
    
    def constant_instantiations(self):
        # Contants

        self.WIDTH = 600
        self.HEIGHT = 600
        self.MAX_FPS = 60

        # Colors

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.IMAGES = {}

    def update_board(self, game, turn):
        self.game = game
        self.draw_board()
        self.draw_pieces()
        # Draw a small circle in the top left corner of the screen to show whose turn it is
        if turn == "Black":
            pygame.draw.circle(self.surface, self.WHITE, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        else:
            pygame.draw.circle(self.surface, self.BLACK, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        pygame.display.update()
        return

    def show_turn(self, turn):
        # Also draw the first circle to represent who goes first
        if turn == "Black":
            pygame.draw.circle(self.surface, self.BLACK, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        else:
            pygame.draw.circle(self.surface, self.WHITE, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)            

    def load_graphics(self):
        # Create constants
        self.constant_instantiations()
        # Draw the board
        self.draw_board()
        # Load the images
        self.load_images()
        # Draw the pieces
        self.draw_pieces()
    
    def reload_graphics(self):
        # Draw the board
        self.draw_board()
        # Draw the pieces
        self.draw_pieces()