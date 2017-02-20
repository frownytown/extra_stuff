import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and hieght of the screen [width, Height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('My game')
# Snow list for snowflake effect

snow_list = []
# snow effect drawing code
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])
# Loop until the user clicks close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Starting position of the rectangle
rect_x = 50
rect_y = 50
# Speed and Direction of rectangle
rect_change_x = 5
rect_change_y = 5
# ----- Main Program loop ----
while not done:
    # --- Main event loop----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ---- Game logic Here ---

    # Screen Clearing code goes here --

    # Here, we clear the screen to white. dont put other drawing commands above
    # this, or they will be erased with this command

    # If you want a background image, replace this clear with blit'ing the
    # background image
    screen.fill(BLACK)

    # Drawing code should go here
    # Processing each snow flake
    for range_var in range(len(snow_list)):

    # Draw snowflake
        pygame.draw.circle(screen, WHITE, snow_list[range_var], 2)

    # Move snowflake down one pixel
        snow_list[range_var][1] += 1

    # If the snow flake has moved off the bottom of the screen
        if snow_list[range_var][1] > 500:
        # Reset it just above top of screen
            y = random.randrange(-50, -10)
            snow_list[range_var][1] = y
        # Give it a new position
            x = random.randrange(0, 700)
            snow_list[range_var][0] = x



    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the rectangle if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Go ahead and update the screen with what we have drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

# Close the window and quit
pygame.quit()
