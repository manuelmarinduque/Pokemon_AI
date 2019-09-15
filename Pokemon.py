import sqlite3 as sql3
import random

matriz_efectividad = [
    [0.5, 0.5, 1, 1, 0.5, 1, 0.5, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1],
    [0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 2, 1, 2, 1, 0.5, 0.5],
    [0.5, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 2],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 2, 1, 0.5, 1, 1, 1, 1],
    [2, 0.5, 2, 0.5, 1, 1, 0.5, 1, 2, 1, 1, 2, 1, 0.5, 1, 1, 1, 1],
    [0.5, 1, 1, 2, 1, 1, 0.5, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
    [0.5, 0.5, 1, 2, 1, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 2, 1, 2],
    [2, 1, 0.5, 1, 1, 0, 1, 0.5, 2, 1, 2, 1, 0.5, 2, 2, 1, 0.5, 0.5],
    [0.5, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1],
    [0.5, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 2, 1, 2, 0.5, 0.5],
    [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1, 0, 1, 2, 1],
    [0.5, 1, 2, 1, 1, 1, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 2],
    [1, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 0.5, 1, 1, 1],
    [2, 1, 0.5, 1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 2, 0],
    [0, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 1],
    [0.5, 1, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 2, 1, 0.5, 1, 1, 1, 1]
]

def Crear_Pokemon():

    conexion = sql3.connect("Pokemon")
    cursor = conexion.cursor()
    pokemones = []

    for i in range(6):
        valor = random.randint(1,100)
        cursor.execute(f"SELECT * FROM Pokemom WHERE Identificator = {valor}")
        pokemones_select = cursor.fetchall()
        fila = list(pokemones_select[0])

        for j in range(4):
            valor2 = random.randint(1,108)
            cursor.execute(f"SELECT * FROM Attacks WHERE Identificator = {valor2}")
            ataques_select = cursor.fetchall()
            fila2 = list(ataques_select[0])
            fila.append(fila2)

        pokemones.append(fila)

    cursor.close()
    conexion.close()
    return pokemones

def damage(pok1, pok2, ataque):

    a = pok1[6]
   
    p = ataque[2]
    d = pok2[7]
    b = 1
    if ataque[4] == pok1[3]:
        b = 1.5
    elif ataque[4] == pok1[4]:
        b = 1.5
    v = random.uniform(85,100)
    e1 = calculo_efectividad(ataque[4], pok1[3])
    e2 = calculo_efectividad(ataque[4], pok1[4])
    e = e1*e2
    damage = 0.01*b*e*v*(((1.02*a*p)/(25.0*d))+2.0)
    return print(f"{damage}, {a}, {p}, {d}, {b}, {v}, {e1}, {e2}")

def calculo_efectividad(tipo_ataque, tipo_pokemon):
    
    if tipo_ataque == 'Acero':
        i = 0
    if tipo_ataque == 'Agua':
        i = 1
    if tipo_ataque == 'Bicho':
        i = 2
    if tipo_ataque == 'Dragon':
        i = 3
    if tipo_ataque == 'Electrico':
        i = 4
    if tipo_ataque == 'Fantasma':
        i = 5
    if tipo_ataque == 'Fuego':
        i = 6
    if tipo_ataque == 'Hada':
        i = 7
    if tipo_ataque == 'Hielo':
        i = 8
    if tipo_ataque == 'Lucha':
        i = 9
    if tipo_ataque == 'Normal':
        i = 10
    if tipo_ataque == 'Planta':
        i = 11
    if tipo_ataque == 'Psiquico':
        i = 12
    if tipo_ataque == 'Roca':
        i = 13
    if tipo_ataque == 'Siniestro':
        i = 14
    if tipo_ataque == 'Tierra':
        i = 15
    if tipo_ataque == 'Veneno':
        i = 16
    if tipo_ataque == 'Volador':
        i = 17
    if tipo_ataque == None:
        return 1
    
    if tipo_pokemon == 'Acero':
        j = 0
    if tipo_pokemon == 'Agua':
        j = 1
    if tipo_pokemon == 'Bicho':
        j = 2
    if tipo_pokemon == 'Dragon':
        j = 3
    if tipo_pokemon == 'Electrico':
        j = 4
    if tipo_pokemon == 'Fantasma':
        j = 5
    if tipo_pokemon == 'Fuego':
        j = 6
    if tipo_pokemon == 'Hada':
        j = 7
    if tipo_pokemon == 'Hielo':
        j = 8
    if tipo_pokemon == 'Lucha':
        j = 9
    if tipo_pokemon == 'Normal':
        j = 10
    if tipo_pokemon == 'Planta':
        j = 11
    if tipo_pokemon == 'Psiquico':
        j = 12
    if tipo_pokemon == 'Roca':
        j = 13
    if tipo_pokemon == 'Siniestro':
        j = 14
    if tipo_pokemon == 'Tierra':
        j = 15
    if tipo_pokemon == 'Veneno':
        j = 16
    if tipo_pokemon == 'Volador':
        j = 17
    if tipo_pokemon == None:
        return 1

    return matriz_efectividad[i][j]

Pokems = Crear_Pokemon()
print(Pokems)
damage(Pokems[0], Pokems[1], Pokems[0][9])

