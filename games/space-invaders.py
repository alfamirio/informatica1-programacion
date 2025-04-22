import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Clase del Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 30])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top, -10, BLANCO)
        todas_sprites.add(bala)
        balas_jugador.add(bala)

# Clase del Invasor
class Invasor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(50, 200)
        self.velocidad_x = random.choice([-2, 2])
        self.contador_movimiento = 0
        self.limite_movimiento = random.randrange(50, 100)
        self.tiempo_disparo = random.randrange(60, 180)

    def update(self):
        self.rect.x += self.velocidad_x
        self.contador_movimiento += 1
        if self.contador_movimiento >= self.limite_movimiento or self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad_x *= -1
            self.rect.y += 30
            self.contador_movimiento = 0
        self.tiempo_disparo -= 1
        if self.tiempo_disparo <= 0:
            self.disparar()
            self.tiempo_disparo = random.randrange(60, 180)
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_x = random.choice([-2, 2])

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.bottom, 5, ROJO)
        todas_sprites.add(bala)
        balas_enemigas.add(bala)

# Clase de la Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad, color):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad = velocidad

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom < 0 or self.rect.top > ALTO:
            self.kill()

# Clase de la Barrera
class Barrera(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 20])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vida = 3  # La barrera soporta 3 impactos

    def recibir_daño(self):
        self.vida -= 1
        if self.vida <= 0:
            self.kill()
        else:
            # Cambiar color según la vida restante
            if self.vida == 2:
                self.image.fill((150, 255, 0))  # Verde más claro
            elif self.vida == 1:
                self.image.fill((100, 255, 0))  # Verde aún más claro

# Grupos de sprites
todas_sprites = pygame.sprite.Group()
invasores = pygame.sprite.Group()
balas_jugador = pygame.sprite.Group()
balas_enemigas = pygame.sprite.Group()
barreras = pygame.sprite.Group()

# Crear jugador
jugador = Jugador()
todas_sprites.add(jugador)

# Crear invasores
for i in range(8):
    invasor = Invasor()
    todas_sprites.add(invasor)
    invasores.add(invasor)

# Crear barreras (4 barreras espaciadas)
for i in range(4):
    barrera = Barrera(150 + i * 150, ALTO - 100)
    todas_sprites.add(barrera)
    barreras.add(barrera)

# Bucle principal
ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.disparar()

    # Actualizar
    todas_sprites.update()

    # Colisiones bala_jugador-invasor
    colisiones = pygame.sprite.groupcollide(invasores, balas_jugador, True, True)
    for colision in colisiones:
        invasor = Invasor()
        todas_sprites.add(invasor)
        invasores.add(invasor)

    # Colisiones bala_jugador-barrera
    for bala in pygame.sprite.groupcollide(balas_jugador, barreras, True, False):
        barrera = pygame.sprite.spritecollideany(bala, barreras)
        if barrera:
            barrera.recibir_daño()

    # Colisiones bala_enemiga-barrera
    for bala in pygame.sprite.groupcollide(balas_enemigas, barreras, True, False):
        barrera = pygame.sprite.spritecollideany(bala, barreras)
        if barrera:
            barrera.recibir_daño()

    # Colisiones bala_enemiga-jugador
    if pygame.sprite.spritecollide(jugador, balas_enemigas, True):
        ejecutando = False

    # Colisiones jugador-invasor
    if pygame.sprite.spritecollide(jugador, invasores, False):
        ejecutando = False

    # Dibujar
    pantalla.fill(NEGRO)
    todas_sprites.draw(pantalla)
    pygame.display.flip()

pygame.quit()
