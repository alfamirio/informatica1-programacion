import random

def mostrar_pregunta(pregunta):
    print("\n" + pregunta["pregunta"])
    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")

def obtener_respuesta_valida():
    while True:
        try:
            respuesta = int(input("Tu respuesta (1-4): "))
            if 1 <= respuesta <= 4:
                return respuesta
            else:
                print("Por favor, elige un número del 1 al 4.")
        except ValueError:
            print("Entrada inválida. Introduce un número del 1 al 4.")

def jugar_trivia():
    preguntas = [
        {
            "pregunta": "¿Cuál es el lenguaje de programación más usado en ciencia de datos?",
            "opciones": ["C++", "Java", "Python", "Ruby"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuál es la capital de Australia?",
            "opciones": ["Sídney", "Melbourne", "Canberra", "Brisbane"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuántos planetas hay en el sistema solar?",
            "opciones": ["7", "8", "9", "10"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "opciones": ["Van Gogh", "Leonardo da Vinci", "Picasso", "Miguel Ángel"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Qué país tiene la mayor población del mundo?",
            "opciones": ["India", "China", "EE.UU.", "Brasil"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Cuál es el símbolo químico del oro?",
            "opciones": ["Go", "Au", "Ag", "Or"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["1935", "1939", "1941", "1945"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Qué órgano del cuerpo humano produce insulina?",
            "opciones": ["Hígado", "Riñón", "Páncreas", "Estómago"],
            "respuesta_correcta": 3
        }
    ]

    random.shuffle(preguntas)
    puntuacion = 0

    print("¡Bienvenido al juego de Trivia!\n")

    for i, pregunta in enumerate(preguntas, start=1):
        print(f"Pregunta {i}:")
        mostrar_pregunta(pregunta)
        respuesta = obtener_respuesta_valida()
        if respuesta == pregunta["respuesta_correcta"]:
            print("¡Correcto!")
            puntuacion += 1
        else:
            correcta = pregunta["opciones"][pregunta["respuesta_correcta"] - 1]
            print(f"Incorrecto. La respuesta correcta era: {correcta}")

    print(f"\nJuego terminado. Tu puntuación fue {puntuacion}/{len(preguntas)}.")

if __name__ == "__main__":
    jugar_trivia()
