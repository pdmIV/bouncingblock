import pygame
import time
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Bouncing Block")
clock = pygame.time.Clock()
running = True
x_pos = random.randint(10, 470)
y_pos = random.randint(10, 470)
x_velocity = 1  # Initial x velocity
y_velocity = 1  # Initial y velocity
rect_width = 50
rect_height = 50
width, height = pygame.display.get_surface().get_size()


def rectangle_move():
    pygame.draw.rect(screen, "white", (x_pos, y_pos, rect_width, rect_height))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    rectangle_move()

    # Update position with velocity
    x_pos += x_velocity
    y_pos += y_velocity

    # Collision detection with walls
    if x_pos <= 0 or x_pos >= width - rect_width:
        x_velocity *= -1  # Reverse x direction

    if y_pos <= 0 or y_pos >= height - rect_height:
        y_velocity *= -1  # Reverse y direction

      

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


