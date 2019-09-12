import sqlite3 as sql3
import random

def Crear_Pokemon():

    conexion = sql3.connect("Pokemon")
    cursor = conexion.cursor()
    pokemones = []

    for i in range(3):
        valor = random.randint(1,100)
        print(valor)
        cursor.execute(f"SELECT * FROM Pokemom WHERE Identificator = {valor}")
        resultado_select = cursor.fetchall()
        fila = list(resultado_select[0])
        pokemones.append(fila)

    cursor.close()
    conexion.close()
    return pokemones

print(Crear_Pokemon())
