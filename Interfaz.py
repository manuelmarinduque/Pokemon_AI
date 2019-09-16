import pygame, sys
from pygame.locals import *
import time
color=(255,255,255)
pygame.init()
#Tamaño de la ventana
ventana=pygame.display.set_mode((500,400))
#titulo
pygame.display.set_caption("Pokemon")
#pokemon 
pok=["nombre",250,"Images/Bulbasaur.png","atac1","atac2","atac3","atac4"]
pok2=["nombre",100,"Images/Charmander.png","atac1","atac2","atac3","atac4"]
#carga imagen del vector2
imagen = pygame.image.load(pok[2])

imagen2 = pygame.image.load(pok2[2])
imagen2 = pygame.transform.scale(imagen2, (90, 90))
imagen = pygame.transform.scale(imagen, (90, 90))
#vida texto
x=pok[1]
y=pok2[1]
miFuente=pygame.font.Font(None,30)
#vida=pygame.font.SysFont("Arial",40)
posX,posY= 320,100

turno=1
contx=0
conty=0

while True:

	ventana.fill(color)
	#nombre y vida
	miTexto=miFuente.render(str(x),0,(200,60,80))
	miTexto2=miFuente.render(pok[0],0,(200,60,80))
	miTexto3=miFuente.render(str(y),0,(200,60,80))
	miTexto4=miFuente.render(pok2[0],0,(200,60,80))
	#ataques
	pygame.draw.rect(ventana, (0,0,0), (25, 25, 220, 80), 5)
	pygame.draw.rect(ventana, (0,0,0), (260, 210, 220, 80), 5)
	pygame.draw.rect(ventana,(0,0,0),(0,300,500,100))
	pygame.draw.rect(ventana,(255,255,255),(10,310,480,80))
	ataque1=miFuente.render(pok[3],0,(200,60,80))
	ataque2=miFuente.render(pok[4],0,(200,60,80))
	ataque3=miFuente.render(pok[5],0,(200,60,80))
	ataque4=miFuente.render(pok[6],0,(200,60,80))

    
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
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			

			if event.key==K_1 and x>0 and turno==1:

				x=x-20
				
				turno=turno-1
			if event.key==K_2 and x>0 and turno==1:

				x=x-10
			

			if event.key==K_3 and x>0 and turno==1:

				x=x-30
				

			if event.key==K_4 and x>0 and turno==1:

				x=x-40
			if turno==1:
				turno=turno-1

			if y>0 and turno==0:
				y=y-20
				turno=turno+1
			if(x<=0 ):
				x=pok[1]
				contx=contx+1
			if(y<=0 ):
				y=pok2[1]
				conty=conty+1

			if(conty==3 or contx==3):
				sys.exit()
    


	#time.sleep(1)
	pygame.display.update()