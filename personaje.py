import random


class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.salud = 100
        self.salud_max = 100
        self.ataque_base = 19
        self.defensa_base = 9
        self.ataque = self.ataque_base
        self.defensa = self.defensa_base
        self.equipamiento = {"arma": None, "armadura": None, "accesorio": None}
        self.inventario = []
        self.dinero = 0
        self.defendiendo = False
        self.experiencia = 0
        self.experiencia_requerida = 100

    def ver_inventario(self):
        print("\nInventario:")
        for i, item in enumerate(self.inventario, 1):
            print(f"{i}. {item.nombre} ({item.tipo})")

        opcion = input("\n¿Qué deseas hacer? (comprar/vender/equipar/salir): ").lower()

        if opcion == "comprar":
            # Lógica de compra de ítems
            pass
        elif opcion == "vender":
            indice_venta = input("Ingresa el número del ítem que deseas vender: ")
            try:
                indice = int(indice_venta) - 1
                self.vender_item(indice)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "equipar":
            self.equipar_item()
        elif opcion == "salir":
            return
        else:
            print("Opción inválida. Intenta de nuevo.")

    def equipar_item(self):
        opcion = input("Ingresa el número del ítem que deseas equipar: ")
        try:
            indice = int(opcion) - 1
            item = self.inventario[indice]

            if item.tipo == "arma":
                self.equipamiento["arma"] = item
                print(f"Has equipado {item.nombre} como tu nueva arma.")
            elif item.tipo == "armadura":
                self.equipamiento["armadura"] = item
                print(f"Has equipado {item.nombre} como tu nueva armadura.")
            elif item.tipo == "accesorio":
                self.equipamiento["accesorio"] = item
                print(f"Has equipado {item.nombre} como tu nuevo accesorio.")
            else:
                print("Este ítem no se puede equipar.")

            self.actualizar_estadisticas()

        except (ValueError, IndexError):
            print("Opción inválida.")

    def atacar(self, enemigo):
        dano = self.ataque - enemigo.defensa
        enemigo.salud -= dano

    def defenderse(self):
        self.defendiendo = True
        print("Te has defendido y reducirás el daño del próximo ataque.")

    def curarse(self, pocion):
        self.salud += pocion.efecto
        if self.salud > self.salud_max:
            self.salud = self.salud_max

    def subir_exp(self, exp_ganada):
        self.experiencia += exp_ganada
        while self.experiencia >= self.experiencia_requerida:
            self.subir_nivel()
            self.experiencia -= self.experiencia_requerida
            self.experiencia_requerida = int(self.experiencia_requerida * 1.1)

    def subir_nivel(self):
        self.nivel += 1
        print(f"¡Felicidades! Has alcanzado el nivel {self.nivel}.")
        self.salud_max += random.randint(1, 3)
        self.salud = self.salud_max
        self.ataque_base += random.randint(1, 3)
        self.defensa_base += random.randint(1, 3)
        self.actualizar_estadisticas()

    def actualizar_estadisticas(self):
        ataque_equipo = 0
        defensa_equipo = 0
        salud_max_equipo = 0

        for item in self.equipamiento.values():
            if item:
                if item.tipo == "arma":
                    ataque_equipo += item.efecto
                elif item.tipo == "armadura":
                    defensa_equipo += item.efecto
                elif item.tipo == "accesorio":
                    salud_max_equipo += item.efecto

        self.ataque = self.ataque_base + ataque_equipo
        self.defensa = self.defensa_base + defensa_equipo
        self.salud_max = self.salud_max + salud_max_equipo
        self.salud = self.salud_max

        print(
            f"Tus nuevas estadísticas son: \nSalud Máxima: {self.salud_max} \nAtaque: {self.ataque} \nDefensa: {self.defensa}"
        )

    def __str__(self):
        return f"Salud: {self.salud} / {self.salud_max} | Defensa: {self.defensa} | Ataque: {self.ataque}\nNivel: {self.nivel} | Dinero: {self.dinero}"


class Item:
    def __init__(self, nombre, tipo, efecto):
        self.nombre = nombre
        self.tipo = tipo
        self.efecto = efecto
