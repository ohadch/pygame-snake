# Pygame Snake Game

![img.png](assets/showcase.png)

This repository contains the source code for a simple snake game implemented using Pygame. The game includes basic features such as movement controls, collision detection with walls and self-collision, and randomly placed food that the snake can eat to grow.

## Features
- **Movement Controls:** Use arrow keys to move the snake in four directions: up, down, left, and right.
- **Food Consumption:** The snake grows longer whenever it consumes food items that appear randomly on the screen.
- **Collision Detection:** The game ends if the snake collides with itself or the boundaries of the game area.

## Setup Instructions
1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository to your local machine using `git clone <repository-url>`.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the game by executing `python main.py` in the terminal.

## Directory Structure
- **src/**: Contains all source code files for the game.
  - **main.py**: Entry point of the game where the main loop is defined.
  - **entities/**: Holds classes for different entities in the game (e.g., Snake, Food).
    - **entity.py**: Base class for all entities with common attributes and methods.
    - **food.py**: Class representing the food item that the snake can consume.
    - **snake.py**: Class representing the main player-controlled entity.
  - **core/**: Houses core components such as positions and vectors used in game mechanics.
