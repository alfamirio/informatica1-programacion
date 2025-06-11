import random

# Tamaño del tablero
TAMANO_TABLERO = 5

# Crear tablero vacío
def crear_tablero():
    return [["~" for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]

# Imprimir tablero
def imprimir_tablero(tablero):
    print("  " + " ".join(str(i) for i in range(TAMANO_TABLERO)))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join(fila))

# Colocar un barco de tamaño variable
def colocar_barco():
    formas = [  # posibles formas del barco
        (1, 2), (2, 1),  # tamaño 2
        (1, 3), (3, 1)   # tamaño 3
    ]
    while True:
        forma = random.choice(formas)
        alto, ancho = forma
        fila_inicio = random.randint(0, TAMANO_TABLERO - alto)
        col_inicio = random.randint(0, TAMANO_TABLERO - ancho)
        posiciones = [(fila_inicio + i, col_inicio + j) for i in range(alto) for j in range(ancho)]
        return posiciones  # solo un barco

# Juego principal
def jugar():
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 6
    aciertos = []

    print("¡Bienvenido a Hundir la flota (versión avanzada)!")
    print("Intenta encontrar el barco de tamaño variable en un tablero 5x5.")
    print("Tienes 6 intentos.")

    for turno in range(intentos):
        imprimir_tablero(tablero)
        try:
            fila = int(input("Adivina la fila (0-4): "))
            col = int(input("Adivina la columna (0-4): "))
        except ValueError:
            print("Entrada inválida. Usa números del 0 al 4.")
            continue

        if (fila, col) in barco:
            if (fila, col) in aciertos:
                print("¡Ya habías acertado esa parte del barco!")
            else:
                print("¡Tocado!")
                tablero[fila][col] = "X"
                aciertos.append((fila, col))
        else:
            print("Agua.")
            if 0 <= fila < TAMANO_TABLERO and 0 <= col < TAMANO_TABLERO:
                tablero[fila][col] = "*"
            else:
                print("Disparo fuera del tablero.")

        if set(aciertos) == set(barco):
            print("¡Felicidades! ¡Has hundido todo el barco!")
            imprimir_tablero(tablero)
            break

        print(f"Intentos restantes: {intentos - turno - 1}\n")
    else:
        print("¡Se acabaron los intentos!")
        print("El barco estaba en las siguientes posiciones:")
        for f, c in barco:
            tablero[f][c] = "B"
        imprimir_tablero(tablero)

# Ejecutar el juego
if __name__ == "__main__":
    jugar()
