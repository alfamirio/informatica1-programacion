import pygame

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Simple")

# Colores
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

# Configuración de la paleta
paddle_width, paddle_height = 100, 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_height)

# Configuración de la bola
ball_size = 10
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_size, ball_size)
ball_speed_x, ball_speed_y = 4, -4

# Configuración de los bloques
block_rows, block_cols = 5, 8
block_width, block_height = WIDTH // block_cols, 30
blocks = [pygame.Rect(col * block_width, row * block_height + 50, block_width - 2, block_height - 2)
          for row in range(block_rows) for col in range(block_cols)]

# Fuente para la puntuación
font = pygame.font.Font(None, 36)
score = 0

# Bucle principal
running = True
clock = pygame.time.Clock()
paddle_speed = 7

while running:
    screen.fill(BLACK)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de la paleta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(paddle_speed, 0)

    # Movimiento de la bola
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Rebotes en los bordes
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Colisiones con los bloques
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y *= -1
            score += 10  # Aumentar puntuación
            break

    # Fin del juego si la bola toca el fondo
    if ball.bottom >= HEIGHT:
        running = False

    # Dibujar elementos
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    # Dibujar la puntuación
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
