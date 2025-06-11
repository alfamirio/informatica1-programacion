import pygame
import sys
import random
import argparse

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Juego de Tres en Raya')
parser.add_argument('-ai', action='store_true', help='Jugar contra IA aleatoria')
args = parser.parse_args()

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 600
ALTO = 600
LINEA_ANCHO = 15
TAMANO_CUADRO = ANCHO // 3
CIRCULO_RADIO = TAMANO_CUADRO // 3
CIRCULO_ANCHO = 15
X_ANCHO = 25
ESPACIO = TAMANO_CUADRO // 4

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Tres en Raya')
pantalla.fill(BLANCO)

# Tablero
tablero = [[None]*3 for _ in range(3)]
jugador = 'X'
ganador = None
juego_terminado = False

# Dibujar líneas del tablero
def dibujar_lineas():
    pygame.draw.line(pantalla, NEGRO, (0, TAMANO_CUADRO), (ANCHO, TAMANO_CUADRO), LINEA_ANCHO)
    pygame.draw.line(pantalla, NEGRO, (0, 2*TAMANO_CUADRO), (ANCHO, 2*TAMANO_CUADRO), LINEA_ANCHO)
    pygame.draw.line(pantalla, NEGRO, (TAMANO_CUADRO, 0), (TAMANO_CUADRO, ALTO), LINEA_ANCHO)
    pygame.draw.line(pantalla, NEGRO, (2*TAMANO_CUADRO, 0), (2*TAMANO_CUADRO, ALTO), LINEA_ANCHO)

# Dibujar figuras
def dibujar_figuras():
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'O':
                pygame.draw.circle(pantalla, AZUL,
                                 (int(col * TAMANO_CUADRO + TAMANO_CUADRO/2),
                                  int(fila * TAMANO_CUADRO + TAMANO_CUADRO/2)),
                                 CIRCULO_RADIO, CIRCULO_ANCHO)
            elif tablero[fila][col] == 'X':
                pygame.draw.line(pantalla, ROJO,
                               (col * TAMANO_CUADRO + ESPACIO, fila * TAMANO_CUADRO + ESPACIO),
                               (col * TAMANO_CUADRO + TAMANO_CUADRO - ESPACIO,
                                fila * TAMANO_CUADRO + TAMANO_CUADRO - ESPACIO), X_ANCHO)
                pygame.draw.line(pantalla, ROJO,
                               (col * TAMANO_CUADRO + TAMANO_CUADRO - ESPACIO, fila * TAMANO_CUADRO + ESPACIO),
                               (col * TAMANO_CUADRO + ESPACIO,
                                fila * TAMANO_CUADRO + TAMANO_CUADRO - ESPACIO), X_ANCHO)

# Verificar ganador
def verificar_ganador():
    global ganador, juego_terminado

    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] and tablero[fila][0] is not None:
            ganador = tablero[fila][0]
            juego_terminado = True
            return

    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] is not None:
            ganador = tablero[0][col]
            juego_terminado = True
            return

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not None:
        ganador = tablero[0][0]
        juego_terminado = True
        return

    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not None:
        ganador = tablero[0][2]
        juego_terminado = True
        return

    if all(tablero[fila][col] is not None for fila in range(3) for col in range(3)):
        ganador = 'Empate'
        juego_terminado = True

# Movimiento de la IA aleatoria
def movimiento_ia():
    global jugador
    if jugador == 'O' and not juego_terminado:
        casillas_vacias = [(fila, col) for fila in range(3) for col in range(3) if tablero[fila][col] is None]
        if casillas_vacias:
            fila, col = random.choice(casillas_vacias)
            tablero[fila][col] = 'O'
            jugador = 'X'
            verificar_ganador()

# Reiniciar juego
def reiniciar():
    global tablero, jugador, ganador, juego_terminado
    pantalla.fill(BLANCO)
    dibujar_lineas()
    tablero = [[None]*3 for _ in range(3)]
    jugador = 'X'
    ganador = None
    juego_terminado = False

# Bucle principal
dibujar_lineas()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
            x, y = evento.pos
            fila = y // TAMANO_CUADRO
            col = x // TAMANO_CUADRO

            if tablero[fila][col] is None:
                tablero[fila][col] = jugador
                jugador = 'O' if jugador == 'X' else 'X'
                verificar_ganador()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                reiniciar()

    # Si está activada la IA y es turno de O
    if args.ai and jugador == 'O':
        movimiento_ia()

    dibujar_figuras()

    if juego_terminado:
        fuente = pygame.font.SysFont(None, 100)
        if ganador == 'Empate':
            texto = fuente.render('Empate!', True, VERDE)
        else:
            texto = fuente.render(f'¡{ganador} gana!', True, VERDE)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2 - texto.get_height()//2))

    pygame.display.update()
