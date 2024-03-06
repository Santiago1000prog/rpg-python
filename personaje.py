import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.salud = 100
        self.ataque = 10
        self.defensa = 5
        self.equipamiento = {'arma': None, 'armadura': None}
        self.inventario = []
        self.dinero = 0
        self.defendiendo = False
        self.experiencia = 0
        self.experiencia_requerida = 100

    def atacar(self, enemigo):
        dano = self.ataque - enemigo.defensa
        enemigo.salud -= dano

    def defenderse(self):
        self.defendiendo = True
        print("Te has defendido y reducirás el daño del próximo ataque.")

    def curarse(self, pocion):
        self.salud += pocion.efecto
        if self.salud > 100:
            self.salud = 100

    def subir_exp(self, exp_ganada):
        self.experiencia += exp_ganada
        while self.experiencia >= self.experiencia_requerida:
            self.subir_nivel()
            self.experiencia -= self.experiencia_requerida
            self.experiencia_requerida = int(self.experiencia_requerida * 1.1)

    def subir_nivel(self):
        self.nivel += 1
        print(f"¡Felicidades! Has alcanzado el nivel {self.nivel}.")
        self.salud += random.randint(1, 3)
        self.ataque += random.randint(1, 3)
        self.defensa += random.randint(1, 3)
        print(f"Tus nuevas estadísticas son: \nSalud: {self.salud} \nAtaque: {self.ataque} \nDefensa: {self.defensa}")


    def __str__(self):
        return f'{self.nombre} (Nivel {self.nivel})'