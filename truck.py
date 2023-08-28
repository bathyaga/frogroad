import pygame


class Truck(pygame.sprite.Sprite):

    # Define constant values
    LEFT_IMAGE = pygame.image.load('resources/RealLeftTruck.png')
    RIGHT_IMAGE = pygame.image.load('resources/RealRightTruck.png')
    STARTING_POSITION = (300, 250)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2

    # Creates a Truck object
    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Truck.LEFT_IMAGE if direction == 'Left' else Truck.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Truck.SIZE)
        # Truck information
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Truck is going left
        if self.direction == 'Left':
            self.rect.centerx -= Truck.MOVE_DIST
            # Truck has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Truck.SCREEN_DIM[0] + (Truck.SIZE[0] / 2)
        # Truck is going right
        else:
            self.rect.centerx += Truck.MOVE_DIST
            # Truck has moved off the screen
            if self.rect.left >= Truck.SCREEN_DIM[0]:
                self.rect.centerx = -Truck.SIZE[0] / 2