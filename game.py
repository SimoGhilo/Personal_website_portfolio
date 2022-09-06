import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Initialization and setting colors

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceships battle')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
SPEED = 5
MISSILE_SPEED = 8
MAX_NUM_MISSILES = 5

# Bar between players

BORDER = pygame.Rect((WIDTH//2-5), 0, 10, HEIGHT)

# Sounds

IMPACT_SOUND = pygame.mixer.Sound(os.path.join('images', 'impact.wav'))
SHOOTING_SOUND = pygame.mixer.Sound(os.path.join('images', 'gun.wav'))


LIFEPOINTS_FONT = pygame.font.SysFont('sans', 30)
WINNER_FONT = pygame.font.SysFont('sans', 50)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 90, 80

# Defining events

PLAYER1_HIT = pygame.USEREVENT + 1
PLAYER2_HIT = pygame.USEREVENT + 2

SPACESHIP_IMAGE1 = pygame.image.load(os.path.join('images', 'spaceship.png'))
SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_IMAGE1, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACESHIP_IMAGE2 = pygame.image.load(
    os.path.join('images', 'spaceship.png'))
SPACESHIP2 = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_IMAGE2, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

''' Background image not adjustable to the screen  '''

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('images', 'backgroundGame.jpg')), (WIDTH, HEIGHT))

# Showing items on the interface


def draw_window(Player_1, Player_2, Player1_missiles, Player2_missiles, Player2_lifepoints, Player1_lifepoints):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    Player2_lifepoints_text = LIFEPOINTS_FONT.render(
        'Health: ' + str(Player2_lifepoints), 1, WHITE)
    Player1_lifepoints_text = LIFEPOINTS_FONT.render(
        'Health: ' + str(Player1_lifepoints), 1, WHITE)
    WIN.blit(Player2_lifepoints_text,
             (WIDTH - Player1_lifepoints_text.get_width() - 10, 10))
    WIN.blit(Player1_lifepoints_text, (10, 10))

    WIN.blit(SPACESHIP1, (Player_1.x, Player_1.y))
    WIN.blit(SPACESHIP2, (Player_2.x, Player_2.y))

    for missile in Player2_missiles:
        pygame.draw.rect(WIN, RED, missile)

    for missile in Player1_missiles:
        pygame.draw.rect(WIN, YELLOW, missile)

    pygame.display.update()


def player_1_movements(keys_pressed, Player_1):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_a] and (Player_1.x - SPEED > 0):  # left
        Player_1.x -= SPEED
    # right
    if keys_pressed[pygame.K_d] and (Player_1.x + SPEED + Player_1.width < BORDER.x):
        Player_1.x += SPEED
    if keys_pressed[pygame.K_w] and (Player_1.y - SPEED > 0):  # up
        Player_1.y -= SPEED
    # down
    if keys_pressed[pygame.K_s] and (Player_1.y + SPEED + Player_1.height < HEIGHT):
        Player_1.y += SPEED


def player_2_movements(keys_pressed, Player_2):
    keys_pressed = pygame.key.get_pressed()
    # left
    if keys_pressed[pygame.K_LEFT] and (Player_2.x - SPEED > BORDER.x + BORDER.width):
        Player_2.x -= SPEED
    # right
    if keys_pressed[pygame.K_RIGHT] and (Player_2.x + SPEED + Player_2.width < WIDTH):
        Player_2.x += SPEED
    if keys_pressed[pygame.K_UP] and (Player_2.y - SPEED > 0):  # up
        Player_2.y -= SPEED
    # down
    if keys_pressed[pygame.K_DOWN] and (Player_2.y + SPEED + Player_2.height < HEIGHT):
        Player_2.y += SPEED


def handle_missiles(Player1_missiles, Player2_missiles, Player_1, Player_2):
    for missile in Player1_missiles:
        missile.x += MISSILE_SPEED
        if Player_2.colliderect(missile):
            pygame.event.post(pygame.event.Event(PLAYER2_HIT))
            Player1_missiles.remove(missile)
        elif missile.x > WIDTH:
            Player1_missiles.remove(missile)

    for missile in Player2_missiles:
        missile.x -= MISSILE_SPEED
        if Player_1.colliderect(missile):
            pygame.event.post(pygame.event.Event(PLAYER1_HIT))
            Player2_missiles.remove(missile)
        elif missile.x < 0:
            Player2_missiles.remove(missile)


def winner(text):
    font_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(font_text, (WIDTH//2 - font_text.get_width() //
             2, HEIGHT//2-font_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(10000)


def main():
    Player_1 = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    Player_2 = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    Player1_missiles = []
    Player2_missiles = []

    Player1_lifepoints = 10
    Player2_lifepoints = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(Player1_missiles) < MAX_NUM_MISSILES:
                    missile = pygame.Rect(
                        Player_1.x + Player_1.width, Player_1.y + Player_1.height//2-2, 10, 5)
                    Player1_missiles.append(missile)
                    SHOOTING_SOUND.play()

                if event.key == pygame.K_RCTRL and len(Player2_missiles) < MAX_NUM_MISSILES:
                    missile = pygame.Rect(
                        Player_2.x, Player_2.y + Player_2.height//2-2, 10, 5)
                    Player2_missiles.append(missile)
                    SHOOTING_SOUND.play()

            if event.type == PLAYER2_HIT:
                Player2_lifepoints -= 1
                IMPACT_SOUND.play()

            if event.type == PLAYER1_HIT:
                Player1_lifepoints -= 1
                IMPACT_SOUND.play()

        win_text = ''
        if Player2_lifepoints <= 0:
            win_text = 'Player 1 is the winner!'

        if Player1_lifepoints <= 0:
            win_text = 'Player 2 is the winner!'

        if win_text != '':
            winner(win_text)
            break

        handle_missiles(Player1_missiles, Player2_missiles, Player_1, Player_2)

        keys_pressed = pygame.key.get_pressed()
        player_1_movements(keys_pressed, Player_1)
        player_2_movements(keys_pressed, Player_2)
        draw_window(Player_1, Player_2, Player1_missiles,
                    Player2_missiles, Player2_lifepoints, Player1_lifepoints)
    main()  # CHECK here


if __name__ == '__main__':
    main()
