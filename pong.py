import sys
import random

import pygame as pygame


def ball_animation():
    global ball_speed_x, ball_speed_y, player1_score, player2_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Player1 Score
    if ball.left <= 0:
        score_time = pygame.time.get_ticks()
        player1_score += 1

    # Player2 Score
    if ball.right >= screen_width:
        score_time = pygame.time.get_ticks()
        player2_score += 1

    # Collide detection and scoring
    if ball.colliderect(player2) and ball_speed_x > 0:
        if abs(ball.right - player2.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(player1) and ball_speed_x < 0:
        if abs(ball.left - player1.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player2_animation():
    player2.y += player2_speed
    if player2.top <= 0:
        player2.top = 0

    if player2.bottom >= screen_height:
        player2.bottom = screen_height


def player1_ai():
    if player1.top < ball.y:
        player1.y += player1_speed
    if player1.bottom > ball.y:
        player1.y -= player1_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


def reset_ball():
    global ball_speed_x, ball_speed_y, ball_moving, score_time
    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = basic_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = basic_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = basic_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None


# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyPong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
player1 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color('black')
light_grey = (211, 211, 211)

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player2_speed = 0
player1_speed = 7
ball_moving = False
score_time = True

# Score Text
player1_score = 0
player2_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

run = True
while run:
    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_DOWN:
                player2_speed += 7
            if event.key == pygame.K_UP:
                player2_speed -= 7

        if event.type == pygame.KEYUP:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_DOWN:
                player2_speed -= 7
            if event.key == pygame.K_UP:
                player2_speed += 7

    ball_animation()
    player2_animation()
    player1_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Scoring
    if score_time:
        reset_ball()

    player1_text = basic_font.render(str(player1_score), False, light_grey)
    screen.blit(player1_text, (660, 470))

    player2_text = basic_font.render(str(player2_score), False, light_grey)
    screen.blit(player2_text, (600, 470))

    # Update window
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
