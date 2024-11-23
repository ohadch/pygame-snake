from src.core.game import Game
from src.settings import SCREEN


if __name__ == '__main__':
    while True:
        game = Game(SCREEN)
        game.run()
