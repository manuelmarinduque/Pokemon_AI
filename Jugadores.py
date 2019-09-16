import Pokemon as pok
import numpy as np


class Ataque:
    def __init__(self, lista=[]):
        self.nombre = lista[1]
        self.potencial = lista[2]
        self.precision = lista[3]
        self.tipo = lista[4]


class Pokemon:
    def __init__(self, lista=[]):
        self.nombre = lista[1]
        self. amount_tipo = lista[2]
        self.tipo1 = lista[3]
        self.tipo2 = lista[4]
        self.vida = lista[5]
        self.ataque = lista[6]
        self.defensa = lista[7]
        self.imagen = lista[8]
        self.vivo = True
        self.ataque1 = Ataque(lista[9])
        self.ataque2 = Ataque(lista[10])
        self.ataque3 = Ataque(lista[11])
        self.ataque4 = Ataque(lista[12])


class Jugador:
    def __init__(self, lista=[]):
        self.pokemon1 = Pokemon(lista[0])
        self.pokemon2 = Pokemon(lista[1])
        self.pokemon3 = Pokemon(lista[2])


def funcionPokemones():
    pk = pok.Crear_Pokemon()

    player = []
    machine = []

    for i in range(3):
        player.append(pk[i])

    for i in range(3, 6):
        machine.append(pk[i])
