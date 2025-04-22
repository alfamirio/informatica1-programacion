import pygame

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de las paletas y la pelota
paleta_ancho, paleta_alto = 10, 100
bola_radio = 10

# Posiciones iniciales
paleta_izq = pygame.Rect(30, ALTO//2 - paleta_alto//2, paleta_ancho, paleta_alto)
paleta_der = pygame.Rect(ANCHO - 40, ALTO//2 - paleta_alto//2, paleta_ancho, paleta_alto)
bola = pygame.Rect(ANCHO//2 - bola_radio, ALTO//2 - bola_radio, bola_radio*2, bola_radio*2)

# Velocidades
velocidad_paleta = 7
velocidad_bola = [5, 5]

# Puntuación
puntos_izq = 0
puntos_der = 0
fuente = pygame.font.Font(None, 50)

# Bucle del juego
jugando = True
while jugando:
    pantalla.fill(NEGRO)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta_izq.top > 0:
        paleta_izq.y -= velocidad_paleta
    if teclas[pygame.K_s] and paleta_izq.bottom < ALTO:
        paleta_izq.y += velocidad_paleta
    if teclas[pygame.K_UP] and paleta_der.top > 0:
        paleta_der.y -= velocidad_paleta
    if teclas[pygame.K_DOWN] and paleta_der.bottom < ALTO:
        paleta_der.y += velocidad_paleta

    # Movimiento de la bola
    bola.x += velocidad_bola[0]
    bola.y += velocidad_bola[1]

    # Colisiones con los bordes superior e inferior
    if bola.top <= 0 or bola.bottom >= ALTO:
        velocidad_bola[1] = -velocidad_bola[1]

    # Colisión con las paletas
    if bola.colliderect(paleta_izq) or bola.colliderect(paleta_der):
        velocidad_bola[0] = -velocidad_bola[0]

    # Verificar si la bola salió de la pantalla
    if bola.left <= 0:  # Punto para el jugador derecho
        puntos_der += 1
        bola.x, bola.y = ANCHO//2, ALTO//2
        velocidad_bola = [5, 5]
    if bola.right >= ANCHO:  # Punto para el jugador izquierdo
        puntos_izq += 1
        bola.x, bola.y = ANCHO//2, ALTO//2
        velocidad_bola = [-5, 5]

    # Dibujar elementos
    pygame.draw.rect(pantalla, BLANCO, paleta_izq)
    pygame.draw.rect(pantalla, BLANCO, paleta_der)
    pygame.draw.ellipse(pantalla, BLANCO, bola)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO))

    # Mostrar puntuación
    texto_izq = fuente.render(str(puntos_izq), True, BLANCO)
    texto_der = fuente.render(str(puntos_der), True, BLANCO)
    pantalla.blit(texto_izq, (ANCHO//4, 20))
    pantalla.blit(texto_der, (ANCHO*3//4, 20))

    # Actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
