import time
import threading

class CookieClicker:
    def __init__(self):
        self.cookies = 0
        self.cps = 0  # Cookies por segundo
        self.upgrades = {
            "cursor": {"price": 10, "cps": 1, "count": 0},
            "grandma": {"price": 100, "cps": 5, "count": 0},
            "factory": {"price": 500, "cps": 20, "count": 0},
            "power_plant": {"price": 2000, "cps": 100, "count": 0},
            "laboratory": {"price": 10000, "cps": 500, "count": 0},
            "robots": {"price": 50000, "cps": 2000, "count": 0},
            "warehouse": {"price": 100000, "cps": 0, "count": 0, "effect": 1.1},  # Mejora pasiva
            "university": {"price": 500000, "cps": 0, "count": 0, "effect": 1.2}  # Mejora global
        }
        self.running = True
        self.lock = threading.Lock()

    def auto_cookies(self):
        while self.running:
            time.sleep(1)
            with self.lock:
                self.cookies += self.cps

    def update_status(self):
        while self.running:
            time.sleep(5)
            with self.lock:
                print(f"\n🍪 Cookies: {self.cookies} | CPS: {self.cps}")
                for name, upgrade in self.upgrades.items():
                    effect = f" (Efecto: {upgrade.get('effect', 1)})" if 'effect' in upgrade else ""
                    print(f"- {name.capitalize()}s: {upgrade['count']} (Coste: {upgrade['price']} cookies){effect}")

    def click(self):
        with self.lock:
            self.cookies += 1
        print("¡Has hecho click! 🍪")

    def buy_upgrade(self, upgrade_name):
        with self.lock:
            if upgrade_name in self.upgrades:
                upgrade = self.upgrades[upgrade_name]
                if self.cookies >= upgrade["price"]:
                    self.cookies -= upgrade["price"]
                    upgrade["count"] += 1
                    self.cps += upgrade["cps"] * upgrade.get("effect", 1)  # Aumentar el cps de las mejoras
                    upgrade["price"] = int(upgrade["price"] * 1.2)  # Incremento del precio
                    print(f"Has comprado una {upgrade_name}.")
                else:
                    print("No tienes suficientes galletas.")
            else:
                print("Esa mejora no existe.")

    def start(self):
        threading.Thread(target=self.auto_cookies, daemon=True).start()
        threading.Thread(target=self.update_status, daemon=True).start()

        while self.running:
            print("\n¿Qué quieres hacer?")
            print("1. Hacer click")
            print("2. Comprar mejora")
            print("3. Salir")
            choice = input("> ")

            if choice == "1":
                self.click()
            elif choice == "2":
                print("¿Qué mejora quieres comprar?")
                for i, name in enumerate(self.upgrades, 1):
                    print(f"{i}. {name.capitalize()}")
                sel = input("> ")
                try:
                    index = int(sel) - 1
                    upgrade_name = list(self.upgrades.keys())[index]
                    self.buy_upgrade(upgrade_name)
                except (ValueError, IndexError):
                    print("Selección inválida.")
            elif choice == "3":
                self.running = False
                print("¡Hasta la próxima!")
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    game = CookieClicker()
    game.start()
