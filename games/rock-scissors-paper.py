import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]

    print("Juego de Piedra, Papel y Tijera")
    print("Elige: piedra, papel o tijera")

    # Elección del usuario
    usuario = input("Tu elección: ").lower()

    # Elección de la computadora
    computadora = random.choice(opciones)

    # Mostrar elecciones
    print(f"Tú: {usuario}")
    print(f"Computadora: {computadora}")

    # Determinar ganador
    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Iniciar el juego
jugar()
