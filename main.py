import random
import pygame

# ========== Pygame Config ==========

WIDTH = 400
HEIGHT = 400
screen_size = [WIDTH, HEIGHT]

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ohad's Snake")

# Set text fonts
score_font = pygame.font.SysFont("monospace", 15)

# ========== Functions ==============


def p5_map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


# ========== Classes =====================


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return self.x, self.y

    def is_clear(self, game_):
        for pos in game_.snake.positions:
            if pos.coordinates == self.coordinates():
                return False
        return True


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __invert__(self):
        return Vector(-self.x, -self.y)


VECTOR_SIZE = 5

RIGHT = Vector(VECTOR_SIZE, 0)
LEFT = Vector(-VECTOR_SIZE, 0)
UP = Vector(0, -VECTOR_SIZE)
DOWN = Vector(0, VECTOR_SIZE)


class Food:

    def __init__(self, game_):
        self.game = game_
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(1, WIDTH - 1)
        y = random.randint(1, HEIGHT - 1)
        p = Position(x, y)
        if p.is_clear(self.game):
            return p
        return self.random_position()

    def show(self):
        pygame.draw.circle(self.game.screen, BLUE, self.position.coordinates(), 5)


class Snake:

    def __init__(self, game_):
        self.game = game_
        self.positions = [Position(WIDTH / 2, HEIGHT / 2)]
        self.vector = RIGHT

    def new_pos(self):
        new_x = self.positions[0].x + self.vector.x
        new_y = self.positions[0].y + self.vector.y
        return Position(new_x, new_y)

    def update(self, eat=False):
        self.positions.insert(0, self.new_pos())
        if eat is False:
            self.positions.pop()

    def eat(self):
        self.update(True)
        self.game.food.position = self.game.food.random_position()

    def is_out_of_boundaries(self):
        return self.positions[0].x == 0 or self.positions[0].x == WIDTH or self.positions[0].y == 0 or self.positions[0].y == HEIGHT

    def is_self_colliding(self):
        for position in self.positions[1:]:
            if self.positions[0].coordinates() == position.coordinates():
                return True
        return False

    def is_colliding(self):
        return self.is_out_of_boundaries() or self.is_self_colliding()

    def show(self):
        for position in self.positions:
            pygame.draw.circle(self.game.screen, RED, position.coordinates(), 5)

    def encounters(self, other, padding):
        if abs(self.positions[0].x - other.position.x) <= padding:
            if abs(self.positions[0].y - other.position.y) <= padding:
                return True
        return False


class Game:

    def __init__(self, screen_, object_padding=10, frame_rate=50):
        self.screen = screen_
        self.snake = Snake(self)
        self.food = Food(self)
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


if __name__ == '__main__':
    while True:
        game = Game(screen)
        game.run()
