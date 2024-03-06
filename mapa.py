class Mapa:
    def __init__(self, dimensiones):
        self.dimensiones = dimensiones
        self.ubicaciones = {}

    def mover_personaje(self, personaje, coordenadas):
        nueva_ubicacion = self.ubicaciones.get(coordenadas)

        if nueva_ubicacion:
            if isinstance(nueva_ubicacion, dict):
                self.procesar_ubicacion(personaje, nueva_ubicacion)
            else:
                print(f"\nHas llegado a: {nueva_ubicacion}")
                print("Parece que aquí no hay nada interesante.")
        else:
            print("No puedes moverte ahí.")

    def procesar_ubicacion(self, personaje, nueva_ubicacion):
        print(f"\nHas llegado a: {nueva_ubicacion['descripcion']}")

        if "items" in nueva_ubicacion:
            print("Encontraste los siguientes ítems:")
            for item in nueva_ubicacion["items"]:
                print(f"- {item.nombre}")
                personaje.inventario.append(item)

        if "dinero" in nueva_ubicacion:
            cantidad_dinero = nueva_ubicacion["dinero"]
            print(f"Encontraste {cantidad_dinero} monedas de oro.")
            personaje.dinero += cantidad_dinero

        if "enemigo" in nueva_ubicacion:
            enemigo = nueva_ubicacion["enemigo"]
            print(f"¡Un {enemigo.nombre} te ha atacado!")
            iniciar_combate(personaje, enemigo)

    def describir_ubicacion(self, coordenadas):
        ubicacion = self.ubicaciones.get(coordenadas)
        return ubicacion if ubicacion else "Ubicación desconocida"
    
            # "enemigo": Enemigo("Lobo Feroz", 30, 8, 2, 15)
    

def iniciar_combate(personaje, enemigo):
    print(f"¡Comienza el combate contra {enemigo.nombre}!")

    while True:
        opcion = input("¿Qué deseas hacer? (atacar/defender/huir): ").lower()

        if opcion == "atacar":
            personaje.atacar(enemigo)
            print(f"Has atacado a {enemigo.nombre} causando {personaje.ataque - enemigo.defensa} puntos de daño.")

            if enemigo.salud <= 0:
                print(f"¡Has derrotado a {enemigo.nombre}!")
                personaje.dinero += enemigo.recompensa
                exp_ganada = enemigo.salud
                personaje.subir_exp(exp_ganada)
                print(f"Has obtenido {enemigo.recompensa} monedas de oro y {exp_ganada} puntos de experiencia.")
                break
            else:
                enemigo.atacar(personaje)

        elif opcion == "defender":
            personaje.defenderse()
            enemigo.atacar(personaje)

        elif opcion == "huir":
            print("Has huido del combate.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

        if personaje.salud <= 0:
            print("¡Has sido derrotado!")
            break