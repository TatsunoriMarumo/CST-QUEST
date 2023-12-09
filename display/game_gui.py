"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import pygame
from creation import character_creation
character = make_character.create_character()

pygame.init()

tile_size = 50
map_size = 15
screen_width = tile_size * map_size
screen_height = tile_size * map_size
font = pygame.font.Font(None, 25)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dungeon RPG")

bg_img = pygame.image.load("images/bg_img.gif")
wall_img = pygame.image.load("images/wall_img.gif")
character_img = pygame.image.load("images/character_img.jpg")

data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

character_position = [1, 1]  # キャラクターの初期位置

running = True
while running:
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            screen.blit(pygame.transform.scale(bg_img, (tile_size, tile_size)), (x * tile_size, y * tile_size))
            if tile == 1:
                screen.blit(pygame.transform.scale(wall_img, (tile_size, tile_size)), (x * tile_size, y * tile_size))
            elif [x, y] == character_position:
                screen.blit(pygame.transform.scale(character_img, (tile_size, tile_size)), (x * tile_size, y * tile_size))

    status_text = f"{character['name']}  HP: {character['status']['current_hp']} / {character['status']['max_hp']}"
    status_surface = font.render(status_text, True, (255, 255, 255))
    screen.blit(status_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and character_position[1] > 0 and data[character_position[1] - 1][character_position[0]] == 0:
                character_position[1] -= 1
            elif event.key == pygame.K_DOWN and character_position[1] < map_size - 1 and data[character_position[1] + 1][character_position[0]] == 0:
                character_position[1] += 1
            elif event.key == pygame.K_LEFT and character_position[0] > 0 and data[character_position[1]][character_position[0] - 1] == 0:
                character_position[0] -= 1
            elif event.key == pygame.K_RIGHT and character_position[0] < map_size - 1 and data[character_position[1]][character_position[0] + 1] == 0:
                character_position[0] += 1

    pygame.display.update()

pygame.quit()
