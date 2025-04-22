import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600  # Resolución actualizada
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fuente para la puntuación
font = pygame.font.Font(None, 36)

# Dirección inicial
dx, dy = BLOCK_SIZE, 0

# Posiciones iniciales
snake = [(100, 100), (80, 100), (60, 100)]
food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
        random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

# Puntuación
score = 0

# Reloj para controlar la velocidad
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -BLOCK_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, BLOCK_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -BLOCK_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = BLOCK_SIZE, 0

    # Mover la serpiente
    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    # Teletransportar la serpiente si toca los bordes
    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

    snake.insert(0, new_head)

    # Verificar colisión con la comida
    if new_head == food:
        food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
        score += 10  # Aumentar puntuación
    else:
        snake.pop()

    # Verificar colisión con el cuerpo
    if new_head in snake[1:]:
        running = False  # Termina el juego si hay colisión

    # Dibujar la serpiente y la comida
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Dibujar puntuación
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Controla la velocidad del juego

pygame.quit()
