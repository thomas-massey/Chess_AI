# This is the where the rendering of the game is done. We will be using OOP

# Imports

import random
from time import sleep
import pygame

class render:
    def __init__(self, game):
        # Load the game
        self.game = game
        self.constant_instantiations()
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        return
    
    def load_images(self):
        pieces = ["Nb", "Rb", "Bb", "Qb", "Kb", "Pb", "Pw", "Rw", "Nw", "Kw", "Qw", "Bw"]
        for piece in pieces:
            # Load the image and then convert it to be a transparent png
            image_loading = pygame.image.load("C:\\Users\\Thomas\\OneDrive - Ardingly College\\Lessons\\U6\\Computer Science\\Personal Projects\\Chess_AI\\images\\" + piece + ".png").convert_alpha()
            self.IMAGES[piece] = pygame.transform.scale(image_loading, (self.WIDTH / 8, self.HEIGHT / 8))
        # We can now access an image by saying 'IMAGES['Pw']'

    def load_promotion_images(self):
        pieces = ["Qw", "Rw", "Bw", "Nw", "Qb", "Rb", "Bb", "Nb"]
        for piece in pieces:
            # Load the image and then convert it to be a transparent png
            image_loading = pygame.image.load("C:\\Users\\Thomas\\OneDrive - Ardingly College\\Lessons\\U6\\Computer Science\\Personal Projects\\Chess_AI\\images\\" + piece + ".png").convert_alpha()
            self.PROMOTION_IMAGES[piece] = pygame.transform.scale(image_loading, (self.WIDTH / 2, self.HEIGHT / 2))
        # We can now access an image by saying 'PROMOTION_IMAGES['Pw']'

    def draw_board(self):
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
                                if full_move in str(move)[0:4]:
                                    if len(str(move)) == 5:
                                        # Render a 2*2 square to show the user what piece they want to promote to
                                        for new_row in range(2):
                                            for new_col in range(2):
                                                if (new_row + new_col) % 2 == 0:
                                                    pygame.draw.rect(self.surface, self.GRAY, (new_col * self.WIDTH / 2, new_row * self.HEIGHT / 2, self.WIDTH / 2, self.HEIGHT / 2))
                                                else:
                                                    pygame.draw.rect(self.surface, self.DARK_GRAY, (new_col * self.WIDTH / 2, new_row * self.HEIGHT / 2, self.WIDTH / 2, self.HEIGHT / 2))
                                        # Now draw the pieces
                                        if turn == "White":
                                            # Draw a white queen in the top left quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Qw"], (0, 0))
                                            # Draw a white rook in the top right quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Rw"], (self.WIDTH / 2, 0))
                                            # Draw a white bishop in the bottom left quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Bw"], (0, self.HEIGHT / 2))
                                            # Draw a white knight in the bottom right quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Nw"], (self.WIDTH / 2, self.HEIGHT / 2))
                                        else:
                                            # Draw a black queen in the top left quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Qb"], (0, 0))
                                            # Draw a black rook in the top right quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Rb"], (self.WIDTH / 2, 0))
                                            # Draw a black bishop in the bottom left quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Bb"], (0, self.HEIGHT / 2))
                                            # Draw a black knight in the bottom right quadrant
                                            self.surface.blit(self.PROMOTION_IMAGES["Nb"], (self.WIDTH / 2, self.HEIGHT / 2))
                                        pygame.display.update()
                                        while True:
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    row = int(pygame.mouse.get_pos()[1] / (self.HEIGHT / 2))
                                                    col = int(pygame.mouse.get_pos()[0] / (self.WIDTH / 2))
                                                    if row == 0 and col == 0:
                                                        return full_move + "q"
                                                    elif row == 0 and col == 1:
                                                        return full_move + "r"
                                                    elif row == 1 and col == 0:
                                                        return full_move + "b"
                                                    else:
                                                        return full_move + "n"
                                                elif event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    quit()
                                                            
                                    return full_move
                    elif len(player_squares) == 0:
                        legal_moves = game.legal_moves
                        origin = chr(int(col)+97) + str(abs((int(row)-8)))
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
                        # Now render the possible locations
                        for move in more_moves:
                            row = abs(int(str(move)[3:4])-8)
                            col = ord(str(move)[2:3]) - 97
                            pygame.draw.rect(self.surface, self.BLUE, (col * self.WIDTH / 8, row * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
                            self.draw_pieces()
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
        self.YELLOW = (255, 255, 0)
        self.CYAN = (0, 255, 255)
        self.MAGENTA = (255, 0, 255)
        self.GRAY = (128, 128, 128)
        self.DARK_GRAY = (64, 64, 64)
        self.IMAGES = {}
        self.PROMOTION_IMAGES = {}

    def update_board(self, game, turn, previous_move):
        self.game = game
        self.draw_board()
        # Draw previous move from opponent - given in for a4b5 format
        if previous_move != None:
            if turn == "White":
                pygame.draw.rect(self.surface, self.RED, (ord(previous_move[2:3]) * self.WIDTH / 8, abs(int(previous_move[3:4])-8) * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
            else:
                pygame.draw.rect(self.surface, self.GREEN, (ord(previous_move[2:3]) * self.WIDTH / 8, abs(int(previous_move[3:4])-8) * self.HEIGHT / 8, self.WIDTH / 8, self.HEIGHT / 8))
        self.draw_pieces()
        # Draw a small circle in the top left corner of the screen to show whose turn it is
        if turn == "Black":
            pygame.draw.circle(self.surface, self.WHITE, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        else:
            pygame.draw.circle(self.surface, self.BLACK, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        pygame.display.update()
        return
    
    def get_turn(self):
        # Split the screen into 4 columns with White, then Black, then Random and then Random VS Random
        pygame.draw.rect(self.surface, self.WHITE, (0, 0, self.WIDTH / 4, self.HEIGHT))
        # Add text to the screen saying White
        #font = pygame.font.SysFont("comicsans", 40)
        #text = font.render("White", 1, self.BLACK)
        #self.surface.blit(text, (self.WIDTH / 8 - text.get_width() / 2, self.HEIGHT / 2 - text.get_height() / 2))
        pygame.draw.rect(self.surface, self.BLACK, (self.WIDTH / 4, 0, self.WIDTH / 4, self.HEIGHT))
        # Add text to the screen saying Black
        #font = pygame.font.SysFont("comicsans", 40)
        #text = font.render("Black", 1, self.WHITE)
        #self.surface.blit(text, (self.WIDTH / 8 - text.get_width() / 2 + self.WIDTH / 4, self.HEIGHT / 2 - text.get_height() / 2))
        pygame.draw.rect(self.surface, self.GRAY, (self.WIDTH / 2, 0, self.WIDTH / 4, self.HEIGHT))
        # Add text to the screen saying Random
        #font = pygame.font.SysFont("comicsans", 40)
        #text = font.render("Random", 1, self.BLACK)
        #self.surface.blit(text, (self.WIDTH / 8 - text.get_width() / 2 + self.WIDTH / 2, self.HEIGHT / 2 - text.get_height() / 2))
        pygame.draw.rect(self.surface, self.RED, (3 * self.WIDTH / 4, 0, self.WIDTH / 4, self.HEIGHT))
        # Add text to the screen saying Chaos
        #font = pygame.font.SysFont("comicsans", 40)
        #text = font.render("Chaos", 1, self.WHITE)
        #self.surface.blit(text, (self.WIDTH / 8 - text.get_width() / 2 + 3 * self.WIDTH / 4, self.HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = int(pygame.mouse.get_pos()[0] // (self.WIDTH / 4))
                    if col == 0:
                        return "White"
                    elif col == 1:
                        return "Black"
                    elif col == 2:
                        colour = random.choice(["White", "Black"])
                        return colour
                    else:
                        return "AIBattle"
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def show_turn(self, turn):
        # Also draw the first circle to represent who goes first
        if turn == "Black":
            pygame.draw.circle(self.surface, self.BLACK, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)
        else:
            pygame.draw.circle(self.surface, self.WHITE, (self.WIDTH / 64, self.HEIGHT / 64), self.WIDTH / 64)            

    def load_graphics(self):
        # Draw the board
        self.draw_board()
        # Load the images
        self.load_images()
        # Load the promotion images
        self.load_promotion_images()
        # Draw the pieces
        self.draw_pieces()
    
    def reload_graphics(self):
        # Draw the board
        self.draw_board()
        # Draw the pieces
        self.draw_pieces()

    def update_display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        # Prevents crashing