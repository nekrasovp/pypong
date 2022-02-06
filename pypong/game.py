import sys
import random

import pygame as pygame

from pypong.menu import MainMenu, OptionsMenu, CreditsMenu


class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.clock = pygame.time.Clock()

        # Main Window
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PyPong")

        # Game Rectangles
        self.ball = pygame.Rect(self.screen_width / 2 - 15, self.screen_height / 2 - 15, 30, 30)
        self.player2 = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        self.player1 = pygame.Rect(10, self.screen_height / 2 - 70, 10, 140)

        # Colors
        self.BLACK_C = (0, 0, 0)
        self.GREY_C = (211, 211, 211)

        # Game Variables
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.player2_speed = 0
        self.player1_speed = 7
        self.ball_moving = False
        self.score_time = True

        # Score Text
        self.player1_score = 0
        self.player2_score = 0
        self.basic_font = pygame.font.Font('pypong/assets/8-BIT WONDER.TTF', 24)

        self.cur_game_screen = 'game'

        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball_speed_y *= -1

        # Player1 Score
        if self.ball.left <= 0:
            self.score_time = pygame.time.get_ticks()
            self.player1_score += 1

        # Player2 Score
        if self.ball.right >= self.screen_width:
            self.score_time = pygame.time.get_ticks()
            self.player2_score += 1

        # Collide detection and scoring
        if self.ball.colliderect(self.player2) and self.ball_speed_x > 0:
            if abs(self.ball.right - self.player2.left) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.bottom - self.player2.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.top - self.player2.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1

        if self.ball.colliderect(self.player1) and self.ball_speed_x < 0:
            if abs(self.ball.left - self.player1.right) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.bottom - self.player1.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.top - self.player1.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1

    def player2_animation(self):
        self.player2.y += self.player2_speed
        if self.player2.top <= 0:
            self.player2.top = 0

        if self.player2.bottom >= self.screen_height:
            self.player2.bottom = self.screen_height

    def player1_ai(self):
        if self.player1.top < self.ball.y:
            self.player1.y += self.player1_speed
        if self.player1.bottom > self.ball.y:
            self.player1.y -= self.player1_speed

        if self.player1.top <= 0:
            self.player1.top = 0
        if self.player1.bottom >= self.screen_height:
            self.player1.bottom = self.screen_height

    def reset_ball(self):
        self.ball.center = (self.screen_width/2, self.screen_height/2)
        current_time = pygame.time.get_ticks()

        if current_time - self.score_time < 700:
            number_three = self.basic_font.render("3", False, self.GREY_C)
            self.screen.blit(number_three, (self.screen_width / 2 - 10, self.screen_height / 2 + 20))
        if 700 < current_time - self.score_time < 1400:
            number_two = self.basic_font.render("2", False, self.GREY_C)
            self.screen.blit(number_two, (self.screen_width / 2 - 10, self.screen_height / 2 + 20))
        if 1400 < current_time - self.score_time < 2100:
            number_one = self.basic_font.render("1", False, self.GREY_C)
            self.screen.blit(number_one, (self.screen_width / 2 - 10, self.screen_height / 2 + 20))

        if current_time - self.score_time < 2100:
            self.ball_speed_y = 0
            self.ball_speed_x = 0
        else:
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.ball_speed_y = 7 * random.choice((1, -1))
            self.score_time = None

    def check_events(self):
        # Inputs
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.cur_game_screen = 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player2_speed += 7
                if event.key == pygame.K_UP:
                    self.player2_speed -= 7
                if event.key == pygame.K_ESCAPE:
                    self.cur_game_screen = 'menu'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player2_speed -= 7
                if event.key == pygame.K_UP:
                    self.player2_speed += 7

    def game_loop(self):
        while self.cur_game_screen == 'game':
            self.check_events()
            self.ball_animation()
            self.player2_animation()
            self.player1_ai()

            # Visuals
            self.screen.fill(self.BLACK_C)
            pygame.draw.rect(self.screen, self.GREY_C, self.player2)
            pygame.draw.rect(self.screen, self.GREY_C, self.player1)
            pygame.draw.ellipse(self.screen, self.GREY_C, self.ball)
            pygame.draw.aaline(self.screen, self.GREY_C, (self.screen_width/2, 0), (self.screen_width/2, self.screen_height))

            # Scoring
            if self.score_time:
                self.reset_ball()

            player1_text = self.basic_font.render(str(self.player1_score), False, self.GREY_C)
            self.screen.blit(player1_text, ((self.screen_width / 2 + 30), (self.screen_height / 2 - 10)))

            player2_text = self.basic_font.render(str(self.player2_score), False, self.GREY_C)
            self.screen.blit(player2_text, ((self.screen_width / 2 - 50), (self.screen_height / 2 - 10)))

            # Update window
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
