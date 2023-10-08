import numpy as np
import random
from variables import *

# Funciones para colocar los barcos

def colocar_barco(barco, tablero):                              
    '''
    Función para colocar los barcos, que tiene como argumentos barco y tablero.
    Devuelve el tablero actualizado
    '''
    for casilla in barco:        
        fila,columna = casilla               
        tablero[fila][columna] = "O"                  
    return tablero

def verificar_superposicion(barco, tablero):
    '''
    Función para verificar que no hay un barco en la casilla.
    Devuelve un True si hay un barco en esa casilla y un False si no.
    '''
    for casilla in barco:
        fila, columna = casilla
        if tablero[fila][columna] == "O":
            return True
    return False

def casilla_valida(fila, columna):
    '''
    Función que sirve para comprobar que las coordenadas no se salen del tablero
    Devuelve las coordenadas si cumplen la condición
    '''
    return 0 <= fila < 10 and 0 <= columna < 10

def crear_barco_random(eslora, tablero):
    '''
    Función que genera los barcos aleatoriamente con su respectiva dirección (N, S, E, O).

    Tiene como argumentos la eslora y el tablero. 

    También llamamos a la función casilla_valida y verificar_superposicion para comprobar si las coordenadas son correctas.

    Devuelve una lista con las coordenadas del barco a colocar en el tablero
    
    '''
    while True:
        fila_random = random.randint(0,9)
        columna_random = random.randint (0,9)

        direccion = random.choice(["N", "S", "E", "O"])
        barco_random = [(fila_random, columna_random)]
        # Aquí le resto uno a la eslora porque ya tengo la primera tupla generada en la variable barco_random
        for _ in range(eslora - 1):         
            if direccion == "N":
                fila_random -= 1
            elif direccion == "S":
                fila_random += 1
            elif direccion == "E":
                columna_random +=1
            elif direccion == "O":
                columna_random -= 1

            casilla = (fila_random, columna_random)
            if not casilla_valida(fila_random, columna_random) or casilla in barco_random or verificar_superposicion(barco_random, tablero):
                break
            barco_random.append(casilla)
        else:                                        
            return barco_random       

def colocar_barcos_en_tablero(tablero, barcos):
    '''
    Función para colocar los barcos en el tablero que utiliza las funciones:
        crear_barco_random y colocar_barco

    Recorre el diccionario barcos con sus valores,
    para generarme la cantidad de barcos que tiene cada uno
    con su correspondiente eslora.

    Devuelve el tablero actualizado con todos los barcos.
    '''
    for _, (eslora, cantidad) in barcos.items():
        # Recorro el diccionario y como es una tupla pongo el () para acceder al contenido de la tupla y no la tupla en si
        for _ in range(cantidad):
            # Aquí itero la cantidad de barcos, para  que me cree los barcos dados en la variable
            barco = crear_barco_random(eslora, tablero)
            tablero = colocar_barco(barco, tablero)
    return tablero                                                 #

# Funciones para disparar

def disparar(tablero, casilla):
    '''
    Función para disparar:
        Pide una fila y una columna para disparar en el tablero enemigo, 
        si aciertas devolvera "Tocado" con una "X" si no, devolvera "Agua" con un "-"
    
    Devuelve el tablero actualizado
    '''

    fila, columna = casilla

    if tablero[fila, columna] == "O":
        print("Tocado")
        tablero[fila, columna] == "X"
        return "Tocado"
    else:
        print("Agua")
        tablero[fila, columna] = "-"
        return "Agua"
    

def comprobar_disparo_cpu(disparos_realizados):
    '''
    Comprobar que el disparo de la CPU es valido y no se repite, es decir que no esta en la variable disparos_realizados.

    Devuelve el disparo aleatorio de la CPU y guarda ese disparo en la variable disparos_realizados
    '''
    while True:
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        casilla = (fila_random, columna_random)

        if casilla not in disparos_realizados:
            disparos_realizados.add(casilla)        #Registra el disparo
            return casilla
        
def mostrar_menu():
    '''
    Función para imprimir por pantalla el menú y iniciar el juego.
    '''

    print("Bienvenido a Hundir la flota")
    print("1. Iniciar juego")
    print("2. Salir")