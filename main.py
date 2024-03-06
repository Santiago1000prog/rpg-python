from personaje import Personaje

heroe = Personaje('Aragorn')
print(heroe)
heroe.subir_exp(390)
print("Experiencia:", heroe.experiencia)
print("Experiencia requerida:", heroe.experiencia_requerida)
heroe.subir_exp(75)
print("Experiencia:", heroe.experiencia)
print("Experiencia requerida:", heroe.experiencia_requerida)