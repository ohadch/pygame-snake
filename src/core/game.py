import pygame

from src.core.vectors import RIGHT, LEFT, UP, DOWN
from src.entities import SnakeEntity, FoodEntity
from src.settings import score_font, BLACK, WHITE, HEIGHT


class Game:

    def __init__(self, screen_, object_padding=10, frame_rate=50):
        self.screen = screen_
        self.snake = SnakeEntity(self)
        self.food = FoodEntity(self)
        self.object_padding = object_padding
        self.frame_rate = frame_rate

    def run(self):
        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()

        # Mainloop
        while not done:

            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(self.frame_rate)

            # Update HUD
            score_label = score_font.render("Score: {}".format(len(self.snake.positions)), 1, BLACK)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN:
                    prev_vector = self.snake.vector
                    if event.key == pygame.K_RIGHT:
                        self.snake.vector = RIGHT
                    elif event.key == pygame.K_LEFT:
                        self.snake.vector = LEFT
                    if event.key == pygame.K_UP:
                        self.snake.vector = UP
                    elif event.key == pygame.K_DOWN:
                        self.snake.vector = DOWN
                    if prev_vector.__invert__().__dict__ == self.snake.vector.__dict__:
                        self.snake.vector = prev_vector

            if self.snake.is_colliding():
                done = True

            if self.snake.encounters(self.food, self.object_padding):
                self.snake.eat()

            # Clear the screen and set the screen background
            self.screen.fill(WHITE)

            # ===========> UPDATE POSITIONS HERE <========

            self.snake.update()

            # ===========> START DRAWING HERE <===========

            self.snake.show()
            self.food.show()
            self.screen.blit(score_label, (15, HEIGHT - 25))

            # ===========> END DRAWING HERE <=============

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
