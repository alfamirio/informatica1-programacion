import pygame
import sys
import textwrap

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El Secreto de la Mazmorra")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)  # Color para victorias
RED = (255, 0, 0)    # Color para derrotas

# Fuente
font = pygame.font.Font(None, 32)

# Clase para manejar el estado del juego
class GameState:
    def __init__(self):
        self.level = 0
        self.choices = []
        self.story = ""

# Textos del juego organizados por niveles (6 niveles de profundidad)
game_content = {
    0: {
        "text": "Eres un aventurero buscando el Cetro de Eldrath, perdido en la Mazmorra de Eldrath. Te enfrentas a su entrada. ¿Qué haces?",
        "options": ["1. Entrar por la puerta principal", "2. Buscar una entrada secreta", "3. Consultar un mapa antiguo"]
    },
    1: {
        "1": {
            "text": "Entras por la puerta principal y encuentras un pasillo bifurcado: uno con marcas de garras y otro con antorchas parpadeantes. ¿Cuál tomas?",
            "options": ["1. Camino con garras", "2. Camino con antorchas"]
        },
        "2": {
            "text": "Buscas y encuentras una trampilla oculta bajo unas rocas. Al abrirla, ves una escalera oscura que desciende. ¿Qué decides?",
            "options": ["1. Bajar por la escalera", "2. Seguir explorando afuera"]
        },
        "3": {
            "text": "Consultas un mapa antiguo que llevas. Revela tres rutas: frontal, lateral y subterránea. ¿Cuál eliges?",
            "options": ["1. Ruta frontal", "2. Ruta lateral", "3. Ruta subterránea"]
        }
    },
    2: {
        "1-1": {
            "text": "El camino con garras te lleva a una sala donde un lobo gigante duerme frente a un cofre. ¿Qué intentas?",
            "options": ["1. Pasar sigilosamente", "2. Atacar al lobo"]
        },
        "1-2": {
            "text": "El camino con antorchas te guía a un puente roto sobre un abismo. Hay una cuerda vieja al lado. ¿Qué haces?",
            "options": ["1. Usar la cuerda para cruzar", "2. Buscar otro camino"]
        },
        "2-1": {
            "text": "Bajas por la escalera y encuentras una cámara con un guardia solitario frente a una puerta. ¿Cómo procedes?",
            "options": ["1. Distraer al guardia", "2. Atacar al guardia"]
        },
        "2-2": {
            "text": "Sigues explorando afuera y encuentras un mercader herido que ofrece información a cambio de ayuda. ¿Lo ayudas?",
            "options": ["1. Sí, ayudarlo", "2. No, ignorarlo"]
        },
        "3-1": {
            "text": "La ruta frontal te lleva a una sala con trampas de flechas activadas por presión. ¿Cómo las enfrentas?",
            "options": ["1. Correr rápido", "2. Avanzar con cuidado"]
        },
        "3-2": {
            "text": "La ruta lateral te lleva a un acantilado con un viejo puente de madera podrida. ¿Qué haces?",
            "options": ["1. Cruzar el puente", "2. Buscar otra ruta"]
        },
        "3-3": {
            "text": "La ruta subterránea te lleva a un túnel inundado. Hay un bote roto al lado. ¿Qué intentas?",
            "options": ["1. Reparar el bote", "2. Nadar"]
        }
    },
    3: {
        "1-1-1": {
            "text": "Pasas sigilosamente y abres el cofre, pero está vacío. Una nota dice: 'El cetro está con el Rey Esqueleto'. ¿Qué haces?",
            "options": ["1. Buscar al Rey Esqueleto", "2. Volver atrás"]
        },
        "1-1-2": {
            "text": "Atacas al lobo, pero está maldito y te infecta con un veneno mortal. Mueres lentamente. Fin.",
            "options": []
        },
        "1-2-1": {
            "text": "Cruzas con la cuerda y llegas a una sala con un pedestal vacío. Una inscripción dice: 'El cetro fue tomado'. ¿Qué haces?",
            "options": ["1. Seguir explorando", "2. Regresar"]
        },
        "1-2-2": {
            "text": "Buscas otro camino, pero el puente colapsa bajo tus pies mientras retrocedes. Caes al abismo. Fin.",
            "options": []
        },
        "2-1-1": {
            "text": "Distraes al guardia y entras. Dentro hay un altar con un cofre sellado mágicamente. ¿Cómo lo abres?",
            "options": ["1. Usar una runa que llevas", "2. Forzar el cofre"]
        },
        "2-1-2": {
            "text": "Atacas al guardia, pero él llama refuerzos. Te capturan y encarcelan en la mazmorra. Fin.",
            "options": []
        },
        "2-2-1": {
            "text": "Ayudas al mercader. Te dice que el cetro está en una cámara sellada abajo. ¿Bajas por la trampilla ahora?",
            "options": ["1. Sí, bajar", "2. No, buscar otra entrada"]
        },
        "2-2-2": {
            "text": "Ignoras al mercader y sigues solo. Te pierdes en el bosque y nunca encuentras la mazmorra otra vez. Fin.",
            "options": []
        },
        "3-1-1": {
            "text": "Corres rápido y evitas las flechas, llegando a una sala con un guardia jefe. ¿Qué haces?",
            "options": ["1. Pelear", "2. Negociar"]
        },
        "3-1-2": {
            "text": "Avanzas con cuidado, pero activas una trampa oculta. Una flecha te atraviesa. Fin.",
            "options": []
        },
        "3-2-1": {
            "text": "Cruzas el puente, que se tambalea pero resiste. Llegas a una cueva con un ermitaño. ¿Le hablas?",
            "options": ["1. Sí, hablar", "2. No, ignorarlo"]
        },
        "3-2-2": {
            "text": "Buscas otra ruta, pero te encuentras con un desprendimiento de rocas que te aplasta. Fin.",
            "options": []
        },
        "3-3-1": {
            "text": "Reparas el bote y navegas hasta una sala con un portal brillante. ¿Entras?",
            "options": ["1. Sí, entrar", "2. No, explorar más"]
        },
        "3-3-2": {
            "text": "Nadas, pero la corriente te arrastra y te ahogas en el túnel. Fin.",
            "options": []
        }
    },
    4: {
        "1-1-1-1": {
            "text": "Buscas al Rey Esqueleto y lo encuentras en un trono. Tiene el cetro. ¿Cómo lo enfrentas?",
            "options": ["1. Pelear directamente", "2. Buscar una debilidad"]
        },
        "1-1-1-2": {
            "text": "Vuelves atrás, pero el lobo despierta y te persigue hasta matarte. Fin.",
            "options": []
        },
        "1-2-1-1": {
            "text": "Exploras más y encuentras un culto secreto adorando el cetro. ¿Qué haces?",
            "options": ["1. Infiltrarte", "2. Atacar al culto"]
        },
        "1-2-1-2": {
            "text": "Regresas, pero el abismo se expande y caes en tu huida. Fin.",
            "options": []
        },
        "2-1-1-1": {
            "text": "Usas la runa y el cofre se abre, pero está vacío. Una voz dice: 'El cetro está más abajo'. ¿Bajas?",
            "options": ["1. Sí, bajar", "2. No, salir"]
        },
        "2-1-1-2": {
            "text": "Fuerzas el cofre, activando una trampa mágica que te quema vivo. Fin.",
            "options": []
        },
        "2-2-1-1": {
            "text": "Bajas por la trampilla y encuentras una sala con dos puertas: una roja y una azul. ¿Cuál eliges?",
            "options": ["1. Puerta roja", "2. Puerta azul"]
        },
        "2-2-1-2": {
            "text": "Buscas otra entrada, pero te pierdes en la noche y mueres de frío. Fin.",
            "options": []
        },
        "3-1-1-1": {
            "text": "Peleas con el guardia jefe y lo derrotas. Encuentras una llave. ¿La usas en la puerta cercana?",
            "options": ["1. Sí, usar la llave", "2. Guardarla"]
        },
        "3-1-1-2": {
            "text": "Negocias con el guardia jefe. Te pide oro a cambio del cetro, pero no tienes suficiente. Te mata. Fin.",
            "options": []
        },
        "3-2-1-1": {
            "text": "Hablas con el ermitaño. Te dice que el cetro está protegido por un dragón. ¿Lo enfrentas?",
            "options": ["1. Sí, buscar al dragón", "2. No, buscar otra forma"]
        },
        "3-2-1-2": {
            "text": "Ignoras al ermitaño y te pierdes en la cueva. Mueres de hambre. Fin.",
            "options": []
        },
        "3-3-1-1": {
            "text": "Entras al portal y apareces en una sala del tesoro custodiada por un golem. ¿Qué haces?",
            "options": ["1. Pelear al golem", "2. Buscar un interruptor"]
        },
        "3-3-1-2": {
            "text": "Exploras más, pero el túnel colapsa y te aplasta. Fin.",
            "options": []
        }
    },
    5: {
        "1-1-1-1-1": {
            "text": "Peleas al Rey Esqueleto y lo derrotas tras una dura batalla. ¡Tomas el Cetro de Eldrath! ¡Ganaste!",
            "options": []
        },
        "1-1-1-1-2": {
            "text": "Buscas una debilidad y encuentras un cristal que lo controla. ¿Lo destruyes?",
            "options": ["1. Sí, destruirlo", "2. No, tomar el cetro directamente"]
        },
        "1-2-1-1-1": {
            "text": "Te infiltras en el culto y robas el cetro durante su ritual. ¡Escapas con éxito! ¡Ganaste!",
            "options": []
        },
        "1-2-1-1-2": {
            "text": "Atacas al culto, pero son demasiados. Te sacrifican en su altar. Fin.",
            "options": []
        },
        "2-1-1-1-1": {
            "text": "Bajas más y encuentras el cetro en una sala sellada. ¡Lo tomas y escapas! ¡Ganaste!",
            "options": []
        },
        "2-1-1-1-2": {
            "text": "Sales, pero la mazmorra colapsa contigo dentro. Fin.",
            "options": []
        },
        "2-2-1-1-1": {
            "text": "Entras por la puerta roja y encuentras el cetro en un pedestal. ¡Lo tomas y vences! ¡Ganaste!",
            "options": []
        },
        "2-2-1-1-2": {
            "text": "Entras por la puerta azul, pero es una trampa. Caes en un pozo de púas. Fin.",
            "options": []
        },
        "3-1-1-1-1": {
            "text": "Usas la llave y entras a una cámara con el cetro. ¡Lo reclamas! ¡Ganaste!",
            "options": []
        },
        "3-1-1-1-2": {
            "text": "Guardas la llave, pero un mecanismo se activa y te aplasta una roca. Fin.",
            "options": []
        },
        "3-2-1-1-1": {
            "text": "Enfrentas al dragón y lo vences con astucia. ¡Tomas el cetro! ¡Ganaste!",
            "options": []
        },
        "3-2-1-1-2": {
            "text": "Buscas otra forma, pero el dragón te encuentra y te incinera. Fin.",
            "options": []
        },
        "3-3-1-1-1": {
            "text": "Peleas al golem y lo destruyes. ¡El cetro es tuyo! ¡Ganaste!",
            "options": []
        },
        "3-3-1-1-2": {
            "text": "Buscas un interruptor y lo encuentras. El golem se desactiva y tomas el cetro. ¡Ganaste!",
            "options": []
        }
    },
    6: {
        "1-1-1-1-2-1": {
            "text": "Destruyes el cristal y el Rey Esqueleto cae. ¡Tomas el Cetro de Eldrath! ¡Ganaste!",
            "options": []
        },
        "1-1-1-1-2-2": {
            "text": "Tomas el cetro directamente, pero el cristal explota y te mata. Fin.",
            "options": []
        }
    }
}

def draw_text(text, y, color=WHITE, max_width=700):
    # Determinar el color basado en el contenido del texto
    if "¡Ganaste!" in text:
        color = GREEN
    elif "Fin." in text:
        color = RED

    wrapped_text = textwrap.fill(text, width=70)
    lines = wrapped_text.split('\n')
    current_y = y
    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (50, current_y))
        current_y += 35
    return current_y

def main():
    game = GameState()
    clock = pygame.time.Clock()
    input_text = ""

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text:
                    if game.level < 5 and input_text in ["1", "2", "3"]:
                        game.choices.append(input_text)
                        game.level += 1
                        input_text = ""
                    elif game.level >= 5:
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode

        # Determinar el contenido actual basado en las elecciones
        if game.level == 0:
            current_content = game_content[0]
        elif game.level == 1:
            current_content = game_content[1][game.choices[0]]
        elif game.level == 2:
            current_content = game_content[2]["-".join(game.choices[:2])]
        elif game.level == 3:
            current_content = game_content[3]["-".join(game.choices[:3])]
        elif game.level == 4:
            current_content = game_content[4]["-".join(game.choices[:4])]
        elif game.level == 5:
            current_content = game_content[5]["-".join(game.choices[:5])]
        elif game.level == 6:
            current_content = game_content[6]["-".join(game.choices[:6])]

        # Dibujar el texto de contexto
        next_y = draw_text(current_content["text"], 30)

        # Dibujar las opciones separadas
        if current_content["options"]:
            next_y += 35
            for option in current_content["options"]:
                next_y = draw_text(option, next_y)
        else:
            next_y = draw_text("Presiona ENTER para reiniciar", next_y + 35)

        # Mostrar entrada del usuario
        draw_text(f"Tu elección: {input_text}", HEIGHT - 100, GRAY)

        # Reiniciar juego si está en el final
        if not current_content["options"] and input_text == "":
            draw_text("Presiona ENTER para reiniciar", HEIGHT - 50, GRAY)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                game = GameState()
                input_text = ""

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
