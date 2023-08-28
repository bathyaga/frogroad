import pygame
from log import Log


class Bear(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/BearPiskel.png')
    STARTING_POSITION = (300, 490)
    SIZE = (20, 10)

    MOVE_DIST = 10
    SCREEN_DIM = 600, 500

    # Creates a frog object
    def __init__(self):
        # sprite setup
        super().__init__()
        self.image = Bear.IMAGE
        self.lives = 3

        # frog rectangle
        self.rect = pygame.Rect((0, 0), Bear.SIZE)
        self.rect.center = Bear.STARTING_POSITION

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Bear.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= Bear.SCREEN_DIM[1] - 20:
            self.rect.centery += Bear.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Bear.MOVE_DIST

    def move_right(self):
        if self.rect.right <= Bear.SCREEN_DIM[0] - 20:
            self.rect.centerx += Bear.MOVE_DIST

    def reset_position(self):
        self.rect.center = Bear.STARTING_POSITION
        self.lives -= 1

    def move_on_log(self, log: Log):
        # Log moving right
        if log.direction == 'Right':
            self.rect.centerx += Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.left >= Log.SCREEN_DIM[0]:
                diff = log.rect.right - self.rect.centerx
                self.rect.centerx = -diff
        # Log moving left
        else:
            self.rect.centerx -= Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.right <= 0:
                diff = abs(log.rect.left - self.rect.centerx)
                self.rect.centerx = Bear.SCREEN_DIM[0] + diff

