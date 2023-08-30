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