class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"\n=== {self.nombre} ===")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)

        if daño < 0:
            daño = 0

        enemigo.vida -= daño

        print(f"{self.nombre} realizó {daño} puntos de daño a {enemigo.nombre}")

        if enemigo.esta_vivo():
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")

    def daño(self, enemigo):
        return (self.fuerza * self.espada) - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"Libro mágico: {self.libro}")

    def daño(self, enemigo):
        return (self.inteligencia * self.libro) - enemigo.defensa


def combate(jugador1, jugador2):

    turno = 1

    while jugador1.esta_vivo() and jugador2.esta_vivo():

        print(f"\n========== TURNO {turno} ==========")

        jugador1.atacar(jugador2)

        if jugador2.esta_vivo():
            jugador2.atacar(jugador1)

        turno += 1

    print("\n========== RESULTADO ==========")

    if jugador1.esta_vivo():
        print(f"Ganador: {jugador1.nombre}")

    elif jugador2.esta_vivo():
        print(f"Ganador: {jugador2.nombre}")

    else:
        print("Empate")


guts = Guerrero("Guts", 20, 10, 4, 100, 4)
vanessa = Mago("Vanessa", 5, 15, 4, 100, 3)

guts.atributos()
vanessa.atributos()

combate(guts, vanessa)
