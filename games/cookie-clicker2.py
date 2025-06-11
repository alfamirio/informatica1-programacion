import time
import os
import sys
import select

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def cookie_clicker():
    cookies = 0
    cps = 0  # Cookies per second
    upgrades = {
        'cursor': {'cost': 10, 'cps': 0.1, 'owned': 0},
        'grandma': {'cost': 100, 'cps': 1, 'owned': 0},
        'farm': {'cost': 1000, 'cps': 10, 'owned': 0},
        'mine': {'cost': 5000, 'cps': 50, 'owned': 0},
        'factory': {'cost': 20000, 'cps': 100, 'owned': 0},
        'bank': {'cost': 100000, 'cps': 500, 'owned': 0},
        'temple': {'cost': 500000, 'cps': 2000, 'owned': 0},
        'wizard': {'cost': 2000000, 'cps': 5000, 'owned': 0}
    }

    print("¡Bienvenido a Cookie Clicker en Terminal!")
    print("Escribe 'c' para hacer click en la galleta, 'u' para comprar mejoras, 'q' para salir.")

    last_time = time.time()

    while True:
        clear_screen()
        print(f"🍪 Galletas: {int(cookies)}")
        print(f"🍪 CPS: {cps:.1f}")
        print("\nMejoras disponibles:")
        for name, data in upgrades.items():
            print(f"{name.capitalize()}: Costo {data['cost']} galletas, CPS +{data['cps']}, Posees: {data['owned']}")
        print("\nEscribe 'c' para click, 'u' para mejoras, 'q' para salir")

        # Actualizar galletas según CPS
        current_time = time.time()
        elapsed_time = current_time - last_time
        cookies += cps * elapsed_time
        last_time = current_time

        # Verificar entrada sin bloquear
        if is_data():
            user_input = sys.stdin.readline().strip().lower()

            if user_input == '':
                cookies += 1
            elif user_input == 'u':
                clear_screen()
                print("Mejoras disponibles:")
                for i, name in enumerate(upgrades, 1):
                    data = upgrades[name]
                    print(f"{i}. {name.capitalize()}: Costo {data['cost']} galletas, CPS +{data['cps']}")
                print("Escribe el número de la mejora para comprar o 'b' para volver")

                while True:
                    if is_data():
                        choice = sys.stdin.readline().strip().lower()
                        if choice == 'b':
                            break
                        try:
                            i = int(choice)
                            if 1 <= i <= len(upgrades):
                                upgrade_name = list(upgrades.keys())[i-1]
                                upgrade = upgrades[upgrade_name]
                                if cookies >= upgrade['cost']:
                                    cookies -= upgrade['cost']
                                    upgrade['owned'] += 1
                                    cps += upgrade['cps']
                                    upgrade['cost'] = int(upgrade['cost'] * 1.15)  # Aumentar costo
                                    print(f"¡Compraste {upgrade_name.capitalize()}!")
                                    time.sleep(1)
                                else:
                                    print("¡No tienes suficientes galletas!")
                                    time.sleep(1)
                                break
                        except ValueError:
                            print("Entrada inválida. Usa un número o 'b' para volver.")
                            time.sleep(1)
            elif user_input == 'q':
                print(f"¡Juego terminado! Galletas totales: {int(cookies)}")
                break

        time.sleep(0.016)  # Aproximadamente 60 FPS

if __name__ == "__main__":
    try:
        cookie_clicker()
    except KeyboardInterrupt:
        print("\n¡Juego terminado!")
