import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
size_screen = (800, 600)
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Управление персонажем")

# Загрузка изображения персонажа
player_image = pygame.image.load("free-icon-superhero-1492447.png")
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()
player_rect.x = size_screen[0] // 2
player_rect.y = size_screen[1] // 2

# Основной игровой цикл
action = True
player_speed = 5
clock = pygame.time.Clock()
while action:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Задний фон
    screen.fill((255, 255, 255))

    # Отображение персонажа на экране
    screen.blit(player_image, player_rect)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
