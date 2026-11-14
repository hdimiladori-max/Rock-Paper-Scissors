import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS")

clock = pygame.time.Clock()

# Colors
BG = (13, 17, 35)
WHITE = (255, 255, 255)
PURPLE = (150, 90, 255)
BLUE = (60, 160, 255)
GREEN = (50, 220, 140)
RED = (255, 75, 95)
GRAY = (45, 52, 75)

# Fonts
title_font = pygame.font.SysFont("Arial", 48, bold=True)
font = pygame.font.SysFont("Arial", 27, bold=True)
small_font = pygame.font.SysFont("Arial", 21)

# Choices
choices = ["ROCK", "PAPER", "SCISSORS"]
symbols = ["✊", "✋", "✌"]

player_score = 0
computer_score = 0

player_choice = "?"
computer_choice = "?"
result = "Choose your move!"
round_number = 1
game_over = False

def draw_text(text, font, color, x, y, center=True):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(image, rect)

def draw_button(rect, color, text, symbol):
    pygame.draw.rect(screen, color, rect, border_radius=18)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=18)

    draw_text(symbol, title_font, WHITE,
              rect.centerx, rect.centery - 22)

    draw_text(text, small_font, WHITE,
              rect.centerx, rect.centery + 35)

def check_winner(player, computer):
    if player == computer:
        return "DRAW"

    if (
        (player == "ROCK" and computer == "SCISSORS")
        or (player == "PAPER" and computer == "ROCK")
        or (player == "SCISSORS" and computer == "PAPER")
    ):
        return "YOU WIN!"

    return "COMPUTER WINS!"

def reset_game():
    global player_score, computer_score
    global player_choice, computer_choice
    global result, round_number, game_over

    player_score = 0
    computer_score = 0
    player_choice = "?"
    computer_choice = "?"
    result = "Choose your move!"
    round_number = 1
    game_over = False

# Buttons
buttons = [
    pygame.Rect(110, 390, 190, 130),
    pygame.Rect(355, 390, 190, 130),
    pygame.Rect(600, 390, 190, 130)
]

restart_button = pygame.Rect(350, 555, 200, 55)

# Main game loop
running = True

while running:

    screen.fill(BG)

    # Background decoration
    pygame.draw.circle(screen, (27, 32, 65), (50, 100), 100)
    pygame.draw.circle(screen, (25, 35, 70), (850, 250), 130)

    draw_text("ROCK PAPER SCISSORS",
              title_font, PURPLE, WIDTH // 2, 55)

    draw_text("PLAYER VS COMPUTER",
              small_font, WHITE, WIDTH // 2, 105)

    # Scoreboard
    pygame.draw.rect(screen, GRAY,
                     (150, 140, 600, 90),
                     border_radius=18)

    draw_text(f"YOU: {player_score}",
              font, GREEN, 300, 175)

    draw_text(f"CPU: {computer_score}",
              font, BLUE, 600, 175)

    # Round
    draw_text(f"ROUND {round_number}",
              small_font, WHITE, WIDTH // 2, 255)

    # Choices display
    draw_text("YOUR CHOICE",
              small_font, GREEN, 280, 300)

    draw_text("COMPUTER",
              small_font, BLUE, 620, 300)

    draw_text(
        symbols[choices.index(player_choice)]
        if player_choice in choices else "?",
        title_font, WHITE, 280, 345
    )

    draw_text(
        symbols[choices.index(computer_choice)]
        if computer_choice in choices else "?",
        title_font, WHITE, 620, 345
    )

    # Selection buttons
    for i, button in enumerate(buttons):
        draw_button(button, GRAY, choices[i], symbols[i])

    # Result
    result_color = (
        GREEN if result == "YOU WIN!"
        else RED if result == "COMPUTER WINS!"
        else BLUE
    )

    if result == "DRAW":
        result_color = WHITE

    draw_text(result, font, result_color,
              WIDTH // 2, 545)

    # Restart button
    pygame.draw.rect(screen, PURPLE,
                     restart_button, border_radius=12)

    draw_text("RESTART",
              small_font, WHITE,
              restart_button.centerx,
              restart_button.centery)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if restart_button.collidepoint(event.pos):
                reset_game()

            elif not game_over:

                for i, button in enumerate(buttons):

                    if button.collidepoint(event.pos):

                        player_choice = choices[i]
                        computer_choice = random.choice(choices)

                        result = check_winner(
                            player_choice, computer_choice
                        )

                        if result == "YOU WIN!":
                            player_score += 1

                        elif result == "COMPUTER WINS!":
                            computer_score += 1

                        round_number += 1

                        if player_score == 3:
                            result = "YOU WON THE MATCH!"
                            game_over = True

                        elif computer_score == 3:
                            result = "COMPUTER WON THE MATCH!"
                            game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
