import pygame, random
from truck import Truck


class Street:
    # Define constant values
    SIZE = (600, 40)
    SCREEN_DIM = 600, 500

    # Creates a Street object
    def __init__(self, street_height: int, direction: str, number_of_trucks: int):
        # Street object
        self.rect = pygame.Rect((0, street_height), Street.SIZE)
        self.trucks = []
        # Add Trucks
        self.add_trucks(direction, number_of_trucks, street_height + 10)

    def add_trucks(self, direction: str, number_of_trucks: int, street_height: int):
        dp = []
        for _ in range(number_of_trucks):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.trucks.append(Truck((x_pos, street_height), direction))