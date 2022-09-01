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
                    
        pygame.display.update()
    
    def get_events(self):
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
                    if clicked_square == (row, col):
                        clicked_square = ()
                        player_squares = []
                    else:
                        clicked_square = (row, col)
                        player_squares.append(clicked_square)
                    if len(player_squares) == 2:
                        return player_squares
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

    def load_graphics(self):
        # Create constants
        self.constant_instantiations()
        # Draw the board
        self.draw_board()
        # Load the images
        self.load_images()
        # Draw the pieces
        self.draw_pieces()