import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minicraft en Python")

# Configuración de los colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Configuración del jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10

# Configuración del reloj
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += 5

    # Actualizar la pantalla
    win.fill(white)
    pygame.draw.rect(win, blue, (player_x, player_y, player_size, player_size))

    # Refrescar la pantalla
    pygame.display.update()

    # Controlar la velocidad del bucle
    clock.tick(30)