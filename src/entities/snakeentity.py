import pygame

from src.core.position import Position
from src.core.vectors import RIGHT
from src.entities.entity import Entity
from src.settings import WIDTH, HEIGHT, RED


class SnakeEntity(Entity):

    def __init__(self, game):
        super().__init__(game)
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
