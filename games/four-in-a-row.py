ROWS = 6
COLS = 7

def crear_tablero():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def imprimir_tablero(tablero):
    print("\n  " + "   ".join(str(i) for i in range(COLS)))
    print(" +" + "---+" * COLS)
    for fila in tablero:
        print(" | " + " | ".join(fila) + " |")
        print(" +" + "---+" * COLS)

def insertar_ficha(tablero, col, ficha):
    for fila in reversed(tablero):
        if fila[col] == " ":
            fila[col] = ficha
            return True
    return False

def es_valido(tablero, col):
    return 0 <= col < COLS and tablero[0][col] == " "

def comprobar_ganador(tablero, ficha):
    # Horizontal
    for f in range(ROWS):
        for c in range(COLS - 3):
            if all(tablero[f][c + i] == ficha for i in range(4)):
                return True
    # Vertical
    for f in range(ROWS - 3):
        for c in range(COLS):
            if all(tablero[f + i][c] == ficha for i in range(4)):
                return True
    # Diagonal /
    for f in range(3, ROWS):
        for c in range(COLS - 3):
            if all(tablero[f - i][c + i] == ficha for i in range(4)):
                return True
    # Diagonal \
    for f in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(tablero[f + i][c + i] == ficha for i in range(4)):
                return True
    return False

def tablero_lleno(tablero):
    return all(c != " " for c in tablero[0])

def jugar():
    tablero = crear_tablero()
    fichas = ["X", "O"]
    turno = 0

    while True:
        imprimir_tablero(tablero)
        jugador = turno % 2
        ficha = fichas[jugador]
        try:
            col = int(input(f"Jugador {jugador + 1} ({ficha}), elige una columna (0-{COLS - 1}): "))
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.")
            continue

        if not es_valido(tablero, col):
            print("Columna no válida o llena. Intenta de nuevo.")
            continue

        insertar_ficha(tablero, col, ficha)

        if comprobar_ganador(tablero, ficha):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador + 1} ({ficha}) ha ganado!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        turno += 1

if __name__ == "__main__":
    jugar()
