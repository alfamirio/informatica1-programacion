def inicio():
    print("Bienvenido a la Cueva Misteriosa.")
    print("Te encuentras en la entrada de una cueva oscura. Hay dos caminos: uno a la izquierda y otro a la derecha.")
    eleccion = input("¿Cuál eliges? (izquierda/derecha): ").strip().lower()

    if eleccion == "izquierda":
        camino_izquierda()
    elif eleccion == "derecha":
        camino_derecha()
    else:
        print("No entiendo tu elección. Intenta de nuevo.")
        inicio()

def camino_izquierda():
    print("\nAvanzas por un pasillo estrecho y llegas a una sala iluminada por antorchas.")
    print("Ves un cofre en el centro de la sala.")
    eleccion = input("¿Quieres abrirlo? (sí/no): ").strip().lower()

    if eleccion == "sí":
        print("¡Has encontrado un tesoro! Eres rico.")
    elif eleccion == "no":
        print("Decides no abrir el cofre y regresas a la entrada.")
        inicio()
    else:
        print("No entiendo tu elección. Intenta de nuevo.")
        camino_izquierda()

def camino_derecha():
    print("\nSigues por un sendero oscuro y escuchas ruidos extraños.")
    print("De repente, un enorme monstruo aparece frente a ti.")
    eleccion = input("¿Quieres luchar o huir? (luchar/huir): ").strip().lower()

    if eleccion == "luchar":
        print("El monstruo es demasiado fuerte y te derrota. Fin del juego.")
    elif eleccion == "huir":
        print("Logras escapar por poco y regresas a la entrada.")
        inicio()
    else:
        print("No entiendo tu elección. Intenta de nuevo.")
        camino_derecha()

# Iniciar el juego
inicio()
