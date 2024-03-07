from personaje import Personaje, Item
from enemigo import Enemigo
from mapa import Mapa


def inicializar_juego():
    nombre_personaje = input("Ingresa el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje)

    # Generar mapa y ubicaciones predeterminadas
    mapa = Mapa((7, 7))
    mapa.ubicaciones = {
        (0, 0): "Ciudad Principal. Aquí comenzó tu aventura.",
        (2, 2): {
            "descripcion": "Bosque Oscuro. Tendrás que estar alerta.",
            "items": [
                Item("Espada Oxidada", "arma", 5),
                Item("Poción Menor", "pocion", 10),
            ],
            "dinero": 20,
            "enemigo": Enemigo("Lobo Feroz", 30, 8, 2, 15),
        },
        (5, 5): "Cueva Misteriosa. ¿Qué secretos esconderá?",
        (0, 3): {
            "descripcion": "Pantano Tenebroso. Un pantano oscuro y peligroso lleno de criaturas peligrosas.",
            "items": [
                Item("Botas de Pantano", "armadura", 5),
                Item("Daga Venenosa", "arma", 7),
                Item("Poción Mayor", "pocion", 50),
            ],
            "dinero": 40,
            "enemigo": Enemigo("Serpiente del Pantano", 50, 8, 5, 30),
        },
        (6, 3): {
            "descripcion": "Cavernas Profundas. Intrincadas cavernas subterráneas que esconden secretos antiguos.",
            "items": [
                Item("Casco de Minero", "armadura", 6),
                Item("Pico Afilado", "arma", 9),
            ],
            "dinero": 70,
            "enemigo": Enemigo("Murciélago Gigante", 55, 9, 6, 35),
        },
        (3, 6): {
            "descripcion": "Pradera Floreciente. Una vasta pradera cubierta de flores silvestres y mariposas.",
            "items": [
                Item("Capa de Flores", "armadura", 4),
                Item("Espada de Pradera", "arma", 6),
            ],
            "dinero": 30,
            "enemigo": Enemigo("Lobo de Pradera", 45, 7, 4, 25),
        },
        (1, 0): {
            "descripcion": "Bosque Sombrío. Un bosque oscuro y tenebroso donde habitan criaturas siniestras.",
            "items": [
                Item("Capucha Siniestra", "armadura", 7),
                Item("Cuchillo Sombrío", "arma", 8),
            ],
            "dinero": 60,
            "enemigo": Enemigo("Elfo Oscuro", 65, 14, 7, 45),
        },
        (5, 5): {
            "descripcion": "Llanura Infinita. Una llanura interminable y despejada, perfecta para viajar.",
            "items": [
                Item("Escudo de Llanura", "armadura", 8),
                Item("Lanza de Llanura", "arma", 10),
            ],
            "dinero": 90,
            "enemigo": Enemigo("Centauro de Llanura", 75, 12, 9, 55),
        },
        (6, 0): {
            "descripcion": "Acantilado Escarpado. Un impresionante acantilado con vistas al mar azul profundo.",
            "items": [
                Item("Botas de Escalador", "armadura", 9),
                Item("Espada del Acantilado", "arma", 11),
            ],
            "dinero": 100,
            "enemigo": Enemigo("Grifo del Acantilado", 85, 13, 10, 65),
        },
    }

    return personaje, mapa


def obtener_nuevas_coordenadas(mapa, posicion_actual):
    direcciones = {"norte": (0, -1), "sur": (0, 1), "este": (1, 0), "oeste": (-1, 0)}
    direccion = input(
        "¿Hacia qué dirección deseas moverte? (norte, sur, este, oeste): "
    ).lower()

    if direccion in direcciones:
        dx, dy = direcciones[direccion]
        nuevas_coordenadas = (posicion_actual[0] + dx, posicion_actual[1] + dy)

        if mapa.coordenada_valida(nuevas_coordenadas):
            return nuevas_coordenadas
        else:
            print("No puedes moverte ahí.", nuevas_coordenadas)
    else:
        print("Dirección inválida.")

    return None


def bucle_principal(personaje, mapa):
    posicion_actual = (0, 0)  # Posición inicial del personaje

    while True:
        print(f"\nEstás en: {mapa.describir_ubicacion(posicion_actual)}")
        print(personaje)
        print("\nOpciones:")
        print("1. Moverte")
        print("2. Ver inventario")
        print("3. Equipar ítem")
        print("4. Salir del juego")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevas_coordenadas = obtener_nuevas_coordenadas(mapa, posicion_actual)
            if nuevas_coordenadas is not None:
                mapa.mover_personaje(personaje, nuevas_coordenadas)
                posicion_actual = nuevas_coordenadas
        elif opcion == "2":
            personaje.ver_inventario()
        elif opcion == "3":
            personaje.equipar_item()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


personaje, mapa = inicializar_juego()
bucle_principal(personaje, mapa)
