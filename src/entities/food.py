import pygame

from src.entities.entity import Entity
from src.settings import BLUE


class FoodEntity(Entity):
    def __init__(self, game):
        super().__init__(game)
        self.position = self.random_position()

    def show(self):
        pygame.draw.circle(self.game.screen, BLUE, self.position.coordinates(), 5)

