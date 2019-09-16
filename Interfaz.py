import pygame, sys
from pygame.locals import *
import time
import Pokemon
import PokemonTree

color=(255,255,255)
pygame.init()

#Tamaño de la ventana
ventana=pygame.display.set_mode((500,400))
#titulo
pygame.display.set_caption("Pokemon")

#pokemon 
pokemones = Pokemon.Crear_Pokemon()
player = []
machine = []

for i in range(3):
    player.append(pokemones[i])

for i in range(3,6):
    machine.append(pokemones[i])

jugador = PokemonTree.Jugador(player)
maquina = PokemonTree.Jugador(machine)

PokemonJugador = jugador.pokemon1
PokemonMaquina = maquina.pokemon1
print(PokemonJugador.nombre, "/", PokemonMaquina.nombre)

#vida texto
x = PokemonMaquina.vida
y = PokemonJugador.vida

while True:
	
	try:
		imagen2 = pygame.image.load(PokemonJugador.imagenTrasera)
		imagen = pygame.image.load(PokemonMaquina.imagenFrente)

		imagen2 = pygame.transform.scale(imagen2, (90, 90))
		imagen = pygame.transform.scale(imagen, (90, 90))

		
		miFuente=pygame.font.Font(None,30)
		#vida=pygame.font.SysFont("Arial",40)
		posX,posY= 320,100

		turno=1
		contx=0
		conty=0

		ventana.fill(color)
		#nombre y vida
		miTexto=miFuente.render(str(x),0,(200,60,80))
		miTexto2=miFuente.render(PokemonMaquina.nombre,0,(200,60,80))
		miTexto3=miFuente.render(str(y),0,(200,60,80))
		miTexto4=miFuente.render(PokemonJugador.nombre,0,(200,60,80))
		#ataques
		pygame.draw.rect(ventana, (0,0,0), (25, 25, 220, 80), 5)
		pygame.draw.rect(ventana, (0,0,0), (260, 210, 220, 80), 5)
		pygame.draw.rect(ventana,(0,0,0),(0,300,500,100))
		pygame.draw.rect(ventana,(255,255,255),(10,310,480,80))
		ataque1=miFuente.render(PokemonJugador.ataque1.nombre,0,(200,0,80))
		ataque2=miFuente.render(PokemonJugador.ataque2.nombre,0,(200,60,80))
		ataque3=miFuente.render(PokemonJugador.ataque3.nombre,0,(200,60,80))
		ataque4=miFuente.render(PokemonJugador.ataque4.nombre,0,(200,60,80))

		ventana.blit(miTexto,(30,30))
		ventana.blit(miTexto3,(430,220))
		ventana.blit(miTexto4,(270,265))
		ventana.blit(miTexto2,(165,80))
		#ataques
		ventana.blit(ataque1,(30,350))
		ventana.blit(ataque2,(150,350))
		ventana.blit(ataque3,(270,350))
		ventana.blit(ataque4,(390,350))
		#imagenes pokemons
		ventana.blit(imagen,(posX,posY))
		ventana.blit(imagen2,(100,210))
		#cuadro para la vida
	
	#--------------------------------------------
	
		perdedor = None
		for event in pygame.event.get():

			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type==pygame.KEYDOWN:
				
				if event.key==K_1 and turno==1:
					x=x-PokemonTree.jugadaJugador(PokemonJugador, PokemonMaquina, PokemonJugador.ataque1)
					turno=2
					
				if event.key==K_2 and turno==1:
					x=x-PokemonTree.jugadaJugador(PokemonJugador, PokemonMaquina, PokemonJugador.ataque2)
					turno=2
					
				if event.key==K_3 and turno==1:
					x=x-PokemonTree.jugadaJugador(PokemonJugador, PokemonMaquina, PokemonJugador.ataque3)
					turno=2
					
				if event.key==K_4 and turno==1:
					x=x-PokemonTree.jugadaJugador(PokemonJugador, PokemonMaquina, PokemonJugador.ataque4)
					turno=2
					
				if turno==2 and x>0:
					ataque = PokemonTree.poderMaquina(PokemonMaquina, PokemonJugador)
					y=y-PokemonTree.jugadaJugador(PokemonMaquina, PokemonJugador, ataque)
					turno=1

				if(x<=0 ):
					PokemonMaquina.vivo = False
					PokemonMaquina = PokemonTree.pokemonUsar(maquina.pokemon1, maquina.pokemon2, maquina.pokemon3)
					if(PokemonMaquina == None):
						perdedor = "Maquina"
						
					x=PokemonMaquina.vida
				if(y<=0 ):
					PokemonJugador.vivo = False
					PokemonJugador = PokemonTree.pokemonUsar(jugador.pokemon1, jugador.pokemon2, jugador.pokemon3)
					if(PokemonJugador == None):
						perdedor = "Jugador"
						
					y=PokemonJugador.vida
	except AttributeError:
		print("El perdedor es ", perdedor)
		break

	pygame.display.update()
