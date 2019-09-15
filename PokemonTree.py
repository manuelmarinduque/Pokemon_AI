import Pokemon


pk = Pokemon.Crear_Pokemon();

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
        while(nivelParada <= 4):
            if(self.listaAbierta == []):
                self.listaAbierta.append(Nodo(self.pokemonContrincante, self.pokemonMaquina, turno))
            else:
                turno = None
                i = len(self.listaAbierta)
                nivelInicial = self.listaAbierta[i-1].nivel
                print("ajajjaajjaja jajajajaja" ,nivelInicial)
                while(nivelInicial  >=  (self.listaAbierta[i-1].nivel)):
                    print(nivelInicial, "|" ,   (self.listaAbierta[i-1].nivel))
                    print(nivelParada)
                    if(self.listaAbierta[i-1].turno == 2):
                        turno = 1
                        self.llenarListaAtaque(self.pokemonMaquina)
                    else:
                        turno = 2
                        self.llenarListaAtaque(self.pokemonContrincante)

                    self.crearNodos(turno, (self.listaAbierta[i-1].nivel)+1, self.listaAbierta[i-1])
                    i-= 1
                    print("nivel", self.listaAbierta[i-1].nivel, len(self.listaAbierta))
                    input()
                
            nivelParada = +1
                

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
    def __init__(self, pkJugador = None, pkMaquina = None, turno=None, nivel = 0, padre = None, ataque=None):
        self.nivel = nivel
        self.turno = turno
        self.pkJugador = pkJugador
        self.pkMaquina = pkMaquina
        self.padre = padre
        self.ataque = ataque

        
        
        
    
class Ataque:
    def __init__(self, lista=[]):
        self.nombre = lista[1] 
        self.potencial = lista[2]
        self.tipo = lista[3]   

class Pokemon:
    def __init__(self, lista = []):
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

###_______________________________________________Funciones_________________________________________________

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

def dañoCausado():
    return 10

def jugadaJugador(pokemonJugador = [], pokemonContrincante = [], ataque=[]):

    daño = pokemonJugador.ataque * dañoCausado()
    pokemonContrincante.vida -= daño 
    if(pokemonContrincante.vida <= 0 ):
        pokemonContrincante.vivo = False


def iniciarJuego():
    jugador = Jugador(player)
    maquina = Jugador(machine)
    pokemonJugador = jugador.pokemon1
    pokemonMaquina = maquina.pokemon1
    turno = 1

    ataqueUsado = ataqueJugador(pokemonJugador.ataque1)
    jugadaJugador(pokemonJugador, pokemonMaquina, ataqueUsado)
    #print(pokemonMaquina.vivo)

    while(victoria(jugador, maquina) == False):
##condicion escojer ´pokemon vivo
        pokemonJugador = pokemonUsar(jugador.pokemon1, jugador.pokemon2, jugador.pokemon3)
        pokemonMaquina = pokemonUsar(maquina.pokemon1, maquina.pokemon2, maquina.pokemon3)

        #print(pokemonMaquina)
        if(turno == 1):
            turno = 2
        else:
            turno = 1

        if (turno == 1):
            ataqueUsado = ataqueJugador(pokemonJugador.ataque1)
            jugadaJugador(pokemonJugador, pokemonMaquina, ataqueUsado)

        if(turno == 2):
            Arbol(pokemonMaquina, pokemonJugador).NodoObjetivo()
            
        break
    
    print("el ganador es ")

    

iniciarJuego()


#H = funcion_daño (precision)
