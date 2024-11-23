import pygame

from src.core.position import Position
from src.core.vector import Vector
from src.entities.entity import Entity
from src.enums import Direction
from src.settings import WIDTH, HEIGHT, RED


class SnakeEntity(Entity):

    def __init__(self, game, speed: int = 2):
        super().__init__(game)
        self._positions = [Position(WIDTH / 2, HEIGHT / 2)]
        self.speed = speed
        self.vector = Vector.from_direction(
            direction=Direction.RIGHT, speed=speed
        )

    def new_pos(self):
        new_x = self._positions[0].x + self.vector.x
        new_y = self._positions[0].y + self.vector.y
        return Position(new_x, new_y)

    def update(self, eat=False):
        self._positions.insert(0, self.new_pos())

        if eat is False:
            self._positions.pop()

    def eat(self):
        self.update(True)
        self.game.food.position = self.game.food.random_position()

    def is_out_of_boundaries(self):
        return self._positions[0].x == 0 or self._positions[0].x == WIDTH or self._positions[0].y == 0 or self._positions[0].y == HEIGHT

    def is_self_colliding(self):
        for position in self._positions[1:]:
            if self._positions[0].coordinates() == position.coordinates():
                return True
        return False

    def is_colliding(self):
        return self.is_out_of_boundaries() or self.is_self_colliding()

    def show(self):
        for position in self._positions:
            pygame.draw.circle(self.game.screen, RED, position.coordinates(), 5)

    def encounters(self, other, padding):
        if abs(self._positions[0].x - other.position.x) <= padding:
            if abs(self._positions[0].y - other.position.y) <= padding:
                return True
        return False

    def update_vector(self, direction: Direction):
        if direction == Direction.UP:
            self.vector = Vector(0, -self.speed)
        elif direction == Direction.DOWN:
            self.vector = Vector(0, self.speed)
        elif direction == Direction.LEFT:
            self.vector = Vector(-self.speed, 0)
        elif direction == Direction.RIGHT:
            self.vector = Vector(self.speed, 0)