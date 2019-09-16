import Pokemon as pok
import numpy as np


pk = pok.Crear_Pokemon()

player = []
machine = []

for i in range(3):
    player.append(pk[i])

for i in range(3,6):
    machine.append(pk[i])

#print(player, "\n")
#print(machine)

class Arbol:
    def __init__(self, pokemonMaquina= None, pokemonContrincante=None):
        self.listaAbierta = []
        self.pokemonMaquina = pokemonMaquina
        self.pokemonContrincante = pokemonContrincante
        self.listaAtaques = []
    
    def NodoObjetivo(self):
        turno = 2
        nivelParada = 0

        while(nivelParada < 4):
            if(self.listaAbierta == []):
                self.listaAbierta.append(Nodo(self.pokemonContrincante, self.pokemonMaquina, turno, 0, None, None, "Raiz"))
            else:
                turno = None
                i = len(self.listaAbierta)
                nivelInicial = self.listaAbierta[i-1].nivel
                
                while(nivelInicial  ==  (self.listaAbierta[i-1].nivel)):
                    print(nivelInicial, "|" ,   (self.listaAbierta[i-1].nivel))
                    print(nivelParada)
                    if(self.listaAbierta[i-1].turno == 2):
                        turno = 1
                        self.llenarListaAtaque(self.pokemonMaquina)
                    else:
                        turno = 2
                        self.llenarListaAtaque(self.pokemonContrincante)
                    if(self.listaAbierta[i-1].tipo != "Aleatorio"):
                        if(turno == 2 and (self.listaAbierta[i-1].nivel)+1 != 4 ):
                            self.listaAbierta.append(nodoAleatorio(self.listaAbierta[i-1], self.listaAbierta[i-1].nivel+1))
                            self.crearNodos(turno, (self.listaAbierta[-1].nivel), self.listaAbierta[-1])
                        else:
                            self.crearNodos(turno, (self.listaAbierta[i-1].nivel)+1, self.listaAbierta[i-1])
                    print("nivel", self.listaAbierta[-1].nivel, len(self.listaAbierta), turno, )
                    i-= 1
                    #input()
                
                nivelParada += 1
                
        
        return self.minMax(self.listaAbierta)

      
    def minMax(self, lista):
        padre = lista[-1].padre
        acumulado = 0
        menor = []
        """for i in range(len(lista)-1, 0,-1):
            if(lista[i].padre.tipo == "Aleatorio" and lista[i].padre == padre):
                acumulado += lista[i].h
            if(lista[i] == padre):
                lista[i].h = definirProbabilidad(acumulado)
                padre = lista[i-1].padre
                acumulado = 0"""

        for i in range(len(lista)-1, 0, -1):


            if(lista[i].padre.tipo == "Aleatorio" and padre.tipo == "Aleatorio"):
                acumulado += lista[i].calificacion
            if(padre != lista[i-1].padre and padre.tipo == "Aleatorio"):
                lista[i].padre.calificacion = definirProbabilidad(acumulado)
                padre = lista[i-1].padre
                menor = []

            if(lista[i].turno == 2 and lista[i] != padre and lista[i].padre.tipo == "Normal") :
                menor.append(lista[i])#menor
            
            if(lista[i].turno == 1 and lista[i] != padre and lista[i].padre.tipo == "Normal"):
                menor.append(lista[i])#mayor
                
            if(lista[i-1].padre != padre and lista[i].turno == 1 and lista[i].tipo == "Normal"):
                lista[i].calificar(mayorLista(menor))
                padre = lista[i-1].padre
                menor=[]

            if(lista[i-1].padre != padre and lista[i].turno == 2 and lista[i].tipo == "Normal"):
                lista[i].calificar(menorLista(menor))
                padre = lista[i-1].padre
                menor = []
            
            if(padre.tipo == "Raiz"):
                menor.append(lista[i])
            if(lista[i].padre == padre and padre.tipo == "Raiz"):
                return lista[i].ataque = ataqueseleccionado(menor)
                
            





    def llenarListaAtaque(self, pokemon):
        self.listaAtaques = []
        self.listaAtaques.append(pokemon.ataque1)
        self.listaAtaques.append(pokemon.ataque2)
        self.listaAtaques.append(pokemon.ataque3)
        self.listaAtaques.append(pokemon.ataque4)
    
    def crearNodos(self,turno, nivel, padre):
        for i in range(len(self.listaAtaques)):
            #print(i)
            self.listaAbierta.append(Nodo(self.pokemonContrincante, self.pokemonMaquina, turno, nivel, padre, self.listaAtaques[i]))




class Nodo:
    def __init__(self, pkJugador = None, pkMaquina = None, turno=None, nivel = 0, padre = None, ataque=None, tipo = "Normal"):
        self.tipo = tipo
        self.nivel = nivel
        self.turno = turno
        self.pkJugador = pkJugador
        self.pkMaquina = pkMaquina
        self.padre = padre
        self.ataque = ataque
        self.h = 0
        self.calificacion = self.h

        if(turno == 1 and padre!= None):
            self.h = np.random.choice([1,0], p=[ataque.precision / 100, 1-(ataque.precision / 100)]) * pok.damage(pkMaquina.ataque, ataque.potencial, pkJugador.defensa, ataque.tipo, pkMaquina.tipo1, pkMaquina.tipo2)
        
        if(turno == 2 and padre != None):
            self.h = np.random.choice([1, 0], p=[ataque.precision / 100, 1-(ataque.precision / 100)]) * pok.damage(pkJugador.ataque, ataque.potencial, pkMaquina.defensa, ataque.tipo, pkJugador.tipo1, pkJugador.tipo2)


    def calificar(self, menor):
        self.calificacion = menor
        
        
class nodoAleatorio:
    def __init__(self, padre=None, nivel = 0):
        self.tipo = "Aleatorio"
        self.h = 0
        self.padre = padre
        self.nivel = nivel
        self.turno = 2     
    
class Ataque:
    def __init__(self, lista=[]):
        self.nombre = lista[1] 
        self.potencial = lista[2]
        self.precision = lista[3]
        self.tipo = lista[4]   

class Pokemon:
    def __init__(self, lista = []):
        self.nombre = lista[1]
        self. amount_tipo = lista[2]
        self.tipo1 = lista[3] 
        self.tipo2 = lista[4]
        self.vida = lista[5]
        self.ataque = lista[6]
        self.defensa = lista[7]
        self.imagenFrente = lista[8]
        self.imagenTrasera = lista[9]
        self.vivo = True
        self.ataque1 = Ataque(lista[10])
        self.ataque2 = Ataque(lista[11])
        self.ataque3 = Ataque(lista[12])
        self.ataque4 = Ataque(lista[13])

class Jugador:
    def __init__(self, lista=[]):
        self.pokemon1 = Pokemon(lista[0])
        self.pokemon2 = Pokemon(lista[1])
        self.pokemon3 = Pokemon(lista[2])

###_______________________________________________Funciones_________________________________________________

def ataqueseleccionado(lista):
    ataque = lista[0].ataque

    print(ataque.nombre)
    return ataque

def mayorLista(lista):
    mayor = lista[0].calificacion
    for i in range(1, len(lista)):
        if(mayor < lista[i].calificacion):
            mayor = lista[i].calificacion

    return mayor

def menorLista(lista):
    menor = lista[0].calificacion
    for i in range(1, len(lista)):
        if(menor > lista[i].calificacion):
            menor = lista[i].calificacion

    return menor

def definirProbabilidad(hTotal):
    return hTotal/4

def pokemonUsar(pokemon1 = [], pokemon2 = [], pokemon3 = [] ):
    pokemon = None
    if(pokemon1.vivo == True):
        return pokemon1
    else:
        if(pokemon2.vivo == True):
            return pokemon2
        else:
            if(pokemon3.vivo == True):
                return pokemon3
    return pokemon

def ataqueJugador(valor = []):
    return valor

def victoria(jugador, maquina):
    if(jugador.pokemon1.vivo == False and jugador.pokemon2.vivo == False and jugador.pokemon3.vivo == False):
        return True

    if(maquina.pokemon1.vivo == False and maquina.pokemon2.vivo == False and maquina.pokemon3.vivo == False):
        return True

    return False


def jugadaJugador(pokemonJugador = None, pokemonContrincante = None, ataque=[]):
    limites = []
    limites.append(1)
    limites.append(0)
    probabilidad = ataque.precision/100.0
    probabilidades = []
    probabilidades.append(probabilidad)
    probabilidades.append(1-probabilidad)

    valorRandom = np.random.choice(limites, p = probabilidades)
    daño = valorRandom *  pok.damage(pokemonJugador.ataque, ataque.potencial, pokemonContrincante.defensa, ataque.tipo, pokemonJugador.tipo1, pokemonJugador.tipo2)
    #print("daño",daño, valorRandom, probabilidad)
    #pokemonContrincante.vida -= daño 
    return daño


def poderMaquina(pokemonMaquina, pokemonContrincante):
    ataque = Arbol(pokemonMaquina, pokemonContrincante).NodoObjetivo()
    print(ataque.nombre)
    return Arbol(pokemonMaquina, pokemonContrincante).NodoObjetivo()
    


#H = funcion_daño (precision)
