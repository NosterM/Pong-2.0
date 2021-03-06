import pygame, sys, random

pygame.font.init()
WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font('freesansbold.ttf', 32)
DETAILS_COLOR = (27, 35, 43)

class GameManager:
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # Drawing the game objects
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # Updating the game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = FONT.render(str(self.player_score), True, DETAILS_COLOR)
        opponent_score = FONT.render(str(self.opponent_score), True, DETAILS_COLOR)

        player_score_rect = player_score.get_rect(midleft=(WIDTH / 2 + 40, HEIGHT / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(WIDTH / 2 - 40, HEIGHT / 2))

        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)

