# Importing pygame modules for the game
import math
import random
import pygame
from pygame import mixer
import os
import sys

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background development/images/sound
bg_image = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\bg_space_seamless_1.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

mixer.music.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\Backgroundsound2.mp3")
mixer.music.play(-1)

pygame.display.set_caption("Space Arc Redemption")
game_icon = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\UFO.jpg")
pygame.display.set_icon(game_icon)

player_image = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\Player.png")
player_x = 410
player_y = 480
player_x_change = 0

enemy_images = []
enemy_x_positions = []
enemy_y_positions = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, (90, 90))  # Resized enemy image
    enemy_images.append(enemy_img)
    enemy_x_positions.append(random.randint(0, 835))
    enemy_y_positions.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

bullet_image = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\redbullet.png")
bullet_image = pygame.transform.scale(bullet_image, (20, 80))  # Resized bullet image
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state, bullet_x
    bullet_state = "fire"
    bullet_x = x
    game_screen.blit(bullet_image, (bullet_x + 8, y + 10))

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def player(x, y):
    game_screen.blit(player_image, (x, y))

def enemy(x, y, i):
    game_screen.blit(enemy_images[i], (x, y))

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    game_screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    game_screen.blit(over_text, (240, 250))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    collision_distance_threshold = 40
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    if distance < collision_distance_threshold:
        return True
    else:
        return False

current_stage = 1
enemy_speed = 2

def show_stage_transition(stage):
    stage_text = over_font.render("STAGE" + " " + str(stage) + " " + "COMPLETED", True, (255, 255, 255))
    game_screen.blit(stage_text, (110, 260))
    pygame.display.update()
    pygame.time.delay(2000)  # Game Pauses for 2 seconds before continuing

def show_intro_screen():
    intro_bg = pygame.image.load("C:\\Users\\newto\\Desktop\\First github pull\\space_arc_redemption\\introbg2.png")
    intro_bg = pygame.transform.scale(intro_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    game_screen.blit(intro_bg, (0, 0))

    intro_font = pygame.font.Font('freesansbold.ttf', 64)
    text_color = (255, 255, 255)  
    outline_color = (0, 0, 0)    #I added an outline and outline color to the into screen text

    intro_text_outline = intro_font.render("Space Arc Redemption", True, outline_color)
    intro_text = intro_font.render("Space Arc Redemption", True, text_color)

    text_x = (SCREEN_WIDTH - intro_text.get_width()) // 2
    text_y = (SCREEN_HEIGHT - intro_text.get_height()) // 2 - 1 * intro_font.get_height()

    game_screen.blit(intro_text_outline, (text_x - 2, text_y))
    game_screen.blit(intro_text_outline, (text_x + 2, text_y))
    game_screen.blit(intro_text_outline, (text_x, text_y - 2))
    game_screen.blit(intro_text_outline, (text_x, text_y + 2))

    game_screen.blit(intro_text, (text_x, text_y))

    pygame.display.update()
    pygame.time.delay(3000)  # Pause for 3 seconds before continuing

show_intro_screen()

def show_start_menu():
    start_font = pygame.font.Font('freesansbold.ttf', 32)
    start_text = start_font.render("Press SPACE to Start", True, (255, 255, 255))
    game_screen.blit(start_text, (280, 300))
    pygame.display.update()

show_start_menu()