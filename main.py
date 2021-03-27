import pygame, sys, random
from gm import GameManager
from Opponent import Opponent
from Ball import Ball
from Player import Player
from Block import Block

# Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Window
WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping-Pong 2.0')

# Variables
BACKGROUND_COLOR = pygame.Color('#2F373F')
DETAILS_COLOR = (27, 35, 43)
FONT = pygame.font.Font('freesansbold.ttf', 32)
PING_SONG = pygame.mixer.Sound("Assets/pong.ogg")
SCORE_SOUND = pygame.mixer.Sound("Assets/score.ogg")
BORDER = pygame.Rect(WIDTH / 2 - 2, 0, 4, HEIGHT)

# Game objects
player = Player('Assets/Paddle.png', WIDTH - 20, HEIGHT / 2, 5)
player_2 = Player('Assets/Paddle.png', 20, WIDTH / 2, 5)
#opponent = Opponent('Paddle.png', 20, WIDTH / 2, 5)
#paddle_group.add(opponent)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(player_2)

ball = Ball('Assets/Ball.png', WIDTH / 2, HEIGHT / 2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.movement -= player.speed
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_2.movement -= player.speed
            if event.key == pygame.K_s:
                player_2.movement += player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_2.movement += player.speed
            if event.key == pygame.K_s:
                player_2.movement -= player.speed

    # Background
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, DETAILS_COLOR, BORDER)

    # Game
    game_manager.run_game()
    pygame.display.flip()
    clock.tick(120)