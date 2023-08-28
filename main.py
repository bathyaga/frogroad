from bear import Bear
from log import Log
from street import Street
from river import River
import pygame, sys, random

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

SCREEN_DIM = WIDTH, HEIGHT = 600, 510
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption('Bear Road!')

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (215, 217, 201)
GREEN = (8, 91, 22)
YELLOW = (137, 147, 13)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (36, 111, 152)

FONT = pygame.font.Font('resources/joystix monospace.ttf', 20)
MENU_BIG = pygame.font.Font('resources/joystix monospace.ttf', 60)
MENU_MED = pygame.font.Font('resources/joystix monospace.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/joystix monospace.ttf', 15)

# Images
MENU_IMAGE = pygame.image.load('resources/BearPiskel.png')
MENU_IMAGE = pygame.transform.scale(MENU_IMAGE, (300,300))

START_MENU = True
END_MENU = False

bear = Bear()

# Create Street objects
streets = []
number_of_trucks = 3
street_height = 400
for _ in range(2):
    streets.append(Street(street_height, 'Left', random.randint(1, number_of_trucks)))
    streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_trucks)))
    street_height -= 80
    
# Create River objects
rivers = []
number_of_logs = 3
river_height = 200
for _ in range(2):
    rivers.append(River(river_height, 'Left', random.randint(1, number_of_logs)))
    rivers.append(River(river_height - 30, 'Right', random.randint(1, number_of_logs)))
    river_height -= 60

score = 0
high_score = 0
current_best = 0

while True:

    while START_MENU:
        # Tick forward at 15 FPS
        CLOCK.tick(15)
        SCREEN.fill(GREEN)

        # Show text on menu screen
        name = MENU_BIG.render('Bear ROAD', True, WHITE)
        instructions = MENU_SMALL.render('Press Space To Start', True, WHITE)
        SCREEN.blit(name, (75, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False

        pygame.display.update()

    while END_MENU:
        # Tick forward at 15 frames per second
        CLOCK.tick(15)

        SCREEN.fill(BLUE)

        # Shoe text on menu
        thx = MENU_MED.render('Thanks for Playing!', True, WHITE)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(instructions, (130, 240))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END_MENU = False
                    bear.lives = 3
                    score = 0
                    current_best = 0


        pygame.display.update()

    CLOCK.tick(FPS)
    SCREEN.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                bear.move_up()
            if event.key == pygame.K_a:  # A
                bear.move_left()
            if event.key == pygame.K_s:  # S
                bear.move_down()
            if event.key == pygame.K_d:  # D
                bear.move_right()



    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for truck in street.trucks:
            SCREEN.blit(truck.image, truck.rect)
            truck.move()
            if bear.rect.colliderect(truck.rect):
                bear.reset_position()

    # Act on rivers and logs
    bear_on_log = False  # new
    for river in rivers:
        # Draw River
        SCREEN.fill(BLUE, river.rect)

        # Log
        for log in river.logs:
            SCREEN.blit(log.image, log.rect)
            log.move()
            if bear.rect.colliderect(log.rect):
                bear.move_on_log(log)
                bear_on_log = True  # new

            # Collided with River and not a Log - new
        if not bear_on_log and bear.rect.colliderect(river.rect):
            bear.reset_position()

    SCREEN.blit(log.image, log.rect)
    SCREEN.blit(bear.image, bear.rect)

    # Update the score only if the score is increasing
    if 475 - bear.rect.top > current_best:
        current_best = 475 - bear.rect.top

    # Frog reached end
    if bear.rect.top <= 60:
        bear.reset_position()
        bear.lives += 1
        score += 1000 + current_best
        current_best = 0

    # Update high score
    if score + current_best >= high_score:
        high_score = score + current_best

    print("Score: " + str(score + current_best))
    print("High Score: " + str(high_score))
    print("Lives: " + str(bear.lives))

    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(bear.lives), True, WHITE)

    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))

    if bear.lives == 0:
        END_MENU = True

    pygame.display.flip()

pygame.quit()