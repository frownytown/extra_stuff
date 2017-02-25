import pygame   # import the pygame module
import time     # import the time module
import random   # import the random module


pygame.init()   # initialize pygame: returns a tuple or success or fail


# Setting up the RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Display Variables
display_width = 800
display_height = 600

# Set the "Canvass" where our game will display: Requires tuple for resolution
game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Slither')   # Setting Title of the game

# Managing screen updating
clock = pygame.time.Clock()


block_size = 10  # Size of our character
fps = 30    # Creating the Frames per second variable

# Creating a font variable for use in our message_to_screen function
font = pygame.font.SysFont(None, 25)


def snake(lead_x, lead_y, block_size):
    """
    Logic for drawing the snake and detecting colision

    :return:
    """
    pygame.draw.rect(game_display, BLACK, [lead_x, lead_y,
                                           block_size, block_size])


def message_to_screen(msg, color):

    """
    Sends a message to the user via the screen when something happens

    :param msg: The contents of the message
    :param color: The color that the message will be
    :return:
    """
    screen_text = font.render(msg, True, color)
    # BLIT = Block Image Transfer, used to draw on the screen
    game_display.blit(screen_text, [display_width / 2, display_height / 2])


# ------------------------ Game Loop ----------------------------- #
def game_loop():
    """
    Main game Loop
    :return:
    """
    game_exit = False  # Initializing game loop exit boolean to false
    game_over = False   # Some game over functionality

    # Starting Position of the snake head
    # The first block x (head of the snake)
    # Rounding so that both the apple and snake appear at a multiple of 10
    lead_x = round((display_width / 2) / 10.0 * 10.0)
    lead_y = round((display_height / 2) / 10.0 * 10.0)    # The first block y
    # Speed and Direction of the snake head
    lead_x_change = 0  # The change of the x coord
    lead_y_change = 0  # The change of the y coord
    # Random apple generation variables
    # Rounding so that both the apple and snake appear at a multiple of 10
    rand_apple_x = round(random.randrange(0, display_width - block_size)
                         / 10.0) * 10.0
    rand_apple_y = round(random.randrange(0, display_height - block_size)
                         / 10.0) * 10.0

    while not game_exit:

        while game_over == True:    # The game over loop
            game_display.fill(WHITE)
            message_to_screen('Game over, press C to play again or Q to quit',
                              GREEN)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    # If q pressed on game over screen exit program
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Checks if QUIT event is clicked
                game_exit = True    # Sets game_exit to True
            if event.type == pygame.KEYDOWN:    # Handling keypress events
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Checks if snake hits the wall then exits if it does
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height \
                or lead_y <= 0:
            game_over = True

        lead_x += lead_x_change    # Updates x position per loop to the new pos
        lead_y += lead_y_change    # Updates y position per loop to the new pos

    # ---------------------- Drawing Code --------------------------------- #
        game_display.fill(WHITE)    # Background
        # Drawing the apples
        pygame.draw.rect(game_display, RED, [rand_apple_x, rand_apple_y,
                                             block_size, block_size])
        # Drawing some stuff on the background
        snake(lead_x, lead_y, block_size)
        pygame.display.update()

        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            print('om nom nom')

        # Frames per second control
        clock.tick(fps)

    # Uninitialize pygame
    pygame.quit()
    quit()      # Exits python

game_loop()


