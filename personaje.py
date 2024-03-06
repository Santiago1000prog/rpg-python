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

    def __str__(self):
        return f'{self.nombre} (Nivel {self.nivel})'