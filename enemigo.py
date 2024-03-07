class Enemigo:
    def __init__(self, nombre, salud, ataque, defensa, recompensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.recompensa = recompensa

    def atacar(self, personaje):
        dano = min(self.ataque - personaje.defensa, 0)
        if personaje.defendiendo:
            dano //= 2  # Reducir el daño a la mitad si el personaje se está defendiendo
            personaje.defendiendo = False
        personaje.salud -= dano
        print(f"{self.nombre} te ha atacado causando {dano} puntos de daño.")