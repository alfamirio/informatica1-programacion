import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxian Mejorado")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)  # Color para disparos de enemigos

# Fuente para la puntuación
font = pygame.font.Font(None, 36)

# Clase para la nave del jugador
class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 60
        self.speed = 5

    def draw(self):
        pygame.draw.rect(window, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

# Clase para los disparos del jugador
class Bullet:
    def __init__(self, x, y):
        self.width = 5
        self.height = 15
        self.x = x + 17
        self.y = y
        self.speed = -7

    def draw(self):
        pygame.draw.rect(window, YELLOW, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

# Clase para los disparos de los enemigos
class EnemyBullet:
    def __init__(self, x, y):
        self.width = 5
        self.height = 15
        self.x = x + 17
        self.y = y
        self.speed = 5

    def draw(self):
        pygame.draw.rect(window, GREEN, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

# Clase para los enemigos
class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed_y = 3
        self.speed_x = 15
        self.moves_left = random.randint(2, 4)
        self.direction = random.choice([-1, 1])
        self.move_counter = 0
        self.move_interval = 20
        self.shoot_counter = 0
        self.shoot_interval = random.randint(60, 120)  # Dispara cada 1-2 segundos

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed_y

        self.move_counter += 1
        if self.moves_left > 0 and self.move_counter >= self.move_interval:
            self.x += self.speed_x * self.direction * 2
            self.x = max(0, min(self.x, WIDTH - self.width))
            self.y -= self.speed_y * 10
            self.moves_left -= 1
            self.move_counter = 0
            self.direction *= -1

    def try_shoot(self):
        self.shoot_counter += 1
        if self.shoot_counter >= self.shoot_interval:
            self.shoot_counter = 0
            return EnemyBullet(self.x, self.y + self.height)
        return None

# Inicialización del juego
player = Player()
enemies = []
bullets = []
enemy_bullets = []
spawn_rate = 60
spawn_counter = 0
score = 0
clock = pygame.time.Clock()
running = True

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x, player.y))

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Generación de enemigos
    spawn_counter += 1
    if spawn_counter >= spawn_rate:
        enemies.append(Enemy())
        spawn_counter = 0

    # Actualizar disparos del jugador
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)

    # Actualizar disparos de enemigos
    for bullet in enemy_bullets[:]:
        bullet.move()
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)

    # Actualizar enemigos
    for enemy in enemies[:]:
        enemy.move()

        # Intento de disparo del enemigo
        new_bullet = enemy.try_shoot()
        if new_bullet:
            enemy_bullets.append(new_bullet)

        # Colisión con jugador
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        if player_rect.colliderect(enemy_rect):
            print(f"¡Juego terminado! Puntuación final: {score}")
            running = False

        # Colisión con disparos del jugador
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
            if enemy_rect.colliderect(bullet_rect):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                break

        # Colisión de disparos enemigos con jugador
        for e_bullet in enemy_bullets[:]:
            e_bullet_rect = pygame.Rect(e_bullet.x, e_bullet.y, e_bullet.width, e_bullet.height)
            if player_rect.colliderect(e_bullet_rect):
                print(f"¡Juego terminado por disparo enemigo! Puntuación final: {score}")
                running = False

        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Dibujar todo
    window.fill(BLACK)
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for e_bullet in enemy_bullets:
        e_bullet.draw()

    # Dibujar puntuación
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
