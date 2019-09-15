import sqlite3 as sql3
import random

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

#Pokems = Crear_Pokemon()
#print(Pokems)

